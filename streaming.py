import json
import sys
from pprint import pprint

import tweepy

import GetWeather_Data
from WeatherBot_Auth import authenticate


def arg_check():
    """
    Checks to see if enough arguments are passed to the program.
    """
    if len(sys.argv) < 2:
        print("Error: Not enough arguments.")
        from usage import usage
        usage()
        sys.exit(1)


class MyStreamListener(tweepy.StreamListener):

    def __init__(self):
        self.count = 0
        self.location_list = []

    def on_connect(self):
        print("Connection established!!")

    def on_disconnect(self, notice):
        print("Connection lost!! : ", notice)

    def on_data(self, data):
        content = json.loads(data)
        arg_check()
        keys_file = sys.argv[1]
        twitter, auth, weather_key = authenticate(keys_file)
        if "direct_message" in content:
            message, id = get_message(content["direct_message"])

            if id != "" and id in self.location_list:
                message, id = get_message(content["direct_message"])
                candidate_locations = GetWeather_Data.location_autocomplete(
                    message)
                if len(candidate_locations["RESULTS"]) == 1:
                    #only one result output
                    get_data_from_location(candidate_locations)
                    self.location_list.remove(id)

                elif len(candidate_locations["RESULTS"]) > 1:
                    #have serveral results output all of them
                    for location in candidate_locations["RESULTS"]:
                        twitter.send_direct_message(user_id=id, text = location["name"])
                    twitter.send_direct_message(user_id=id, text = "Please choose one and send it again")


                else:
                    #have no results
                    twitter.send_direct_message(user_id=id, text = "Can't find request location,\
                    please input 'location' keywords and try again")
                    self.location_list.remove(id)

            elif message != "" and id != "":
                record_id = message_analyze(message, id)
                self.location_list.append(record_id)

        return True

    def on_direct_message(self, status):
        print("Enter on_direct_message")
        print status
        return True

    def on_error(self, status):
        print (statuses)


def get_message(content):
    if "id" in content:
        message = twitter.get_direct_message(content["id"])
        return message["text"], content["sender_id_str"]
    return "", ""


def message_analyze(message, id):
    if message == 'location':
        arg_check()
        keys_file = sys.argv[1]
        twitter, auth, weather_key = authenticate(keys_file)
        text = "Please input location"
        twitter.send_direct_message(user=id, text=text)
        return id


def get_data_from_location(location):
    """
    get weahter data from request location
    """
    arg_check()
    keys_file = sys.argv[1]
    twitter, auth, weather_key = authenticate(keys_file)
    return GetWeather_Data.get_weather_data(api_key=weather_key,
                                            request_type="conditions",
                                            location=location["RESULTS"][0][l])

if __name__ == "__main__":
    # the following just test case
    arg_check()

    keys_file = sys.argv[1]
    twitter, auth, weather_key = authenticate(keys_file)

    l = MyStreamListener()
    stream = tweepy.Stream(auth, l)
    stream.userstream()
