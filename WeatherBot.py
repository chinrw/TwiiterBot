#!/usr/bin/env python

import sys
import requests
import os

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

def get_current_weather(location, request_type):
    """
    return a string which contains current weather
    """
    arg_check()

    keys_file = sys.argv[1]
    twitter, auth, weather_key = authenticate(keys_file)

    data = get_weather_data(weather_key, request_type, location)

    location = data["current_observation"]["display_location"]["full"]
    weahter  = data["current_observation"]["weather"]
    feeltemp = data["current_observation"]['windchill_string']
    temp     = data["current_observation"]['temperature_string']
    time     = data["current_observation"]["observation_time"]
    wind     = data["current_observation"]["wind_string"]
    humi     = data["current_observation"]["relative_humidity"]
    url      = data["current_observation"]["icon_url"]

    tweet_output = location + '\n' + time + '\n' + temp + '\n' + "feeling like "\
        + feeltemp + '\n' + wind + '\n'

    return tweet_output

def main():
    """
    update twitter status on timeline.
    """
    arg_check()

    keys_file = sys.argv[1]
    twitter, auth, weather_key = authenticate(keys_file)

    location = '/q/zmw:12180.1.99999'
    data = get_weather_data(weather_key, request_type, location)
    request_type = "conditions"

    location = data["current_observation"]["display_location"]["full"]
    weahter  = data["current_observation"]["weather"]
    feeltemp = data["current_observation"]['windchill_string']
    temp     = data["current_observation"]['temperature_string']
    time     = data["current_observation"]["observation_time"]
    wind     = data["current_observation"]["wind_string"]
    humi     = data["current_observation"]["relative_humidity"]
    url      = data["current_observation"]["icon_url"]

    tweet_output = location + '\n' + time + '\n' + temp + '\n' + "feeling like "\
        + feeltemp + '\n' + wind + '\n'
    filename = 'temp.jpg'

    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)

    print(tweet_output)

    twitter.update_with_media(filename=filename,status=tweet_output)
    os.remove(filename)


# ============================================================================ #
if __name__ == "__main__":
    main()
