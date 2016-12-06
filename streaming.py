import tweepy
import sys
import json
from pprint import pprint
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

    def on_connect(self):
        print("Connection established!!")

    def on_disconnect(self, notice):
        print("Connection lost!! : ", notice)

    def on_data(self, data):
        content = json.loads(data)
        if "direct_message" in content:
            pprint(content)
            direct_message_analyze(content["direct_message"])
        return True

    def on_direct_message(self, status):
        print("Enter on_direct_message")
        print status
        return True

    def on_error(self, status):
        print (statuses)

def direct_message_analyze(content):
    if "id" in content:
        message = twitter.get_direct_message(content["id"])
        return message["text"]
    return data


if __name__ == "__main__":

    arg_check()

    keys_file = sys.argv[1]
    twitter, auth, weather_key = authenticate(keys_file)

    l = MyStreamListener()
    stream = tweepy.Stream(auth, l)
    stream.userstream()
