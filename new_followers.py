#!/usr/bin/env python
# encoding: utf-8
import json
import sys
import time

from WeatherBot_Auth import authenticate


"""
send message if someone follows us
"""


def arg_check():
    """
    Checks to see if enough arguments are passed to the program.
    """
    if len(sys.argv) < 2:
        print("Error: Not enough arguments.")
        from usage import usage
        usage()
        sys.exit(1)


def new_followers_check():
    arg_check()

    keys_file = sys.argv[1]

# import data from file
    with open("followers.json", 'r') as i:
        data = json.load(i)

# pull data from twitter
    twitter, auth, weather_key = authenticate(keys_file)
    followers_id = twitter.followers_ids()["ids"]

# find the changes in followers
    changes = set(followers_id) - set(data)
    if list(changes) and changes.issubset(set(followers_id)):
        for id in list(changes):
            twitter.send_direct_message(
                user_id=id, text="Thank you for following us")
                # send message to new followers

    with open("followers.json", 'w') as f:
        json.dump(followers_id, f)


if __name__ == "__main__":
    for i in range(0, 500):
        new_followers_check()
        time.sleep(15)
