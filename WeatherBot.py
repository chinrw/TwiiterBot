#!/usr/bin/env python

import os
import requests
import sched
import sys
import time

from GetWeather_Data import get_weather_data
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

def get_current_weather(request_type="conditions",\
                        location="/q/zmw:12180.1.99999"):
    """
    Returns a string with current weather information for tweet.
    """
    keys_file = sys.argv[1]
    twitter, weather_key = authenticate(keys_file)

    data = get_weather_data(weather_key, request_type, location)

    location  = data["current_observation"]["display_location"]["full"]
    weahter   = data["current_observation"]["weather"]
    windchill = data["current_observation"]['windchill_string']
    temp      = data["current_observation"]['temperature_string']
    time      = data["current_observation"]["observation_time"]
    wind      = data["current_observation"]["wind_string"]
    humi      = data["current_observation"]["relative_humidity"]
    icon_url  = data["current_observation"]["icon_url"]

    icon_file = 'temp.jpg'
    request = requests.get(icon_url, stream=True)
    if request.status_code == 200:
        with open(icon_file, 'wb') as image:
            for chunk in request:
                image.write(chunk)

    tweet_text = location + '\n' \
               + time     + '\n' \
               + temp     + '\n' \
               + "Feels like " + windchill + '\n'\
               + wind + '\n'

    return twitter, icon_file, tweet_text

def tweet():
    """
    Tweets from text and image input.
    """
    twitter_api, icon_file, tweet_text = get_current_weather()

    print(tweet_text)

    if len(icon_file) > 0:
        twitter_api.update_with_media(filename=icon_file, status=tweet_text)
        os.remove(filename)

    else:
        twitter_api.update(status=tweet_text)

def scheduled_tweet(minutes):
    """
    Tweets iteratively every given amount of minutes.
    """
    s = sched.scheduler(time.time, time.sleep)
    s.enter(60*minutes, 1, tweet, ())
    s.run()

def run():
    """
    Main function to run the program.
    update twitter status on timeline.
    """
    arg_check()

    if len(sys.argv) > 2:
        minutes = sys.argv[2]
        scheduled_tweet(minutes)

    else:
        tweet()

# ============================================================================ #
if __name__ == "__main__":
    run()
