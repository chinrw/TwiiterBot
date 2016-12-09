import json
import sys
import time
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

    def __init__(self, twitter, auth, weather_key):
        self.count = 0
        self.location_list = []
        self.twitter, self.auth, self.weather_key = twitter, auth, weather_key

    def on_connect(self):
        print("Connection established!!")

    def on_disconnect(self, notice):
        print("Connection lost!! : ", notice)

    def on_data(self, data):
        content = json.loads(data)
        twitter, auth, weather_key = self.twitter, self.auth, self.weather_key
        if "direct_message" in content:
            message, id = get_message(content["direct_message"], self.twitter)

            if id != "" and id in self.location_list:
                message, id = get_message(
                    content["direct_message"], self.twitter)
                candidate_locations = GetWeather_Data.location_autocomplete(
                    message)
                if len(candidate_locations["RESULTS"]) == 1:
                    # only one result output
                    get_data_from_location(
                        candidate_locations, self.twitter, self.weather_key)
                    self.location_list.remove(id)

                elif len(candidate_locations["RESULTS"]) > 1:
                    # have serveral results output all of them
                    for location in candidate_locations["RESULTS"]:
                        self.twitter.send_direct_message(
                            user_id=id, text=location["name"])
                        time.sleep(1)
                    self.twitter.send_direct_message(
                        user_id=id, text="Please choose one and send it again")

                else:
                    # have no results
                    self.twitter.send_direct_message(user_id=id, text="Can't find request location,\
                    please input 'location' keywords and try again")
                    self.location_list.remove(id)

            elif message != "" and id != "":
                record_id = message_analyze(message, id, self.twitter)
                self.location_list.append(record_id)

        return True

    def on_error(self, status):
        print (statuses)

    def on_timeout(self):
        sys.stderr.write("Timeout, sleeping for 60 seconds...\n")
        time.sleep(60)
        return


def get_message(content, twitter):
    if "id" in content:
        message = twitter.get_direct_message(content["id"])
        return message["text"], content["sender_id_str"]
    return "", ""


def message_analyze(message, id, twitter):
    if message == 'location':
        text = "Please input location"
        twitter.send_direct_message(user=id, text=text)
        return id


def get_data_from_location(location, twitter, weather_key):
    """
    get weahter data from request location
    """
    return GetWeather_Data.get_weather_data(api_key=weather_key,
                                            request_type="conditions",
                                            location=location["RESULTS"][0]["l"])


def run_stream(twitter, auth, weather_key):
    l = MyStreamListener(twitter, auth, weather_key)
    stream = tweepy.Stream(auth=auth, listener=l)
    stream.userstream()


if __name__ == "__main__":
    # the following just test case
    arg_check()

    keys_file = sys.argv[1]
    twitter, auth, weather_key = authenticate(keys_file)
    run_stream(twitter, auth, weather_key)
