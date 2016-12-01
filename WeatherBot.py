#!/usr/bin/env python

import sys
from WeatherBot_Auth import authenticate
from GetWeather_Data import get_weather_data

def arg_check():
    """
    Checks to see if enough arguments are passed to the program.
    """
    if len(sys.argv) < 2:
        print("Error: Not enough arguments.")
        from usage import usage
        usage()
        sys.exit(1)

def main():
    """
    Main function for WeatherBot.
    """
    arg_check()

    keys_file = sys.argv[1]
    twitter, weather_key = authenticate(keys_file)

    # weather_key = 'f4d95466fcf4f1dc'
    weather_key = '3dfa9f9c19a712ac'
    data = get_weather_data(weather_key)

    location = data["current_observation"]["display_location"]["full"]
    wind     = data["current_observation"]['windchill_string']
    temp     = data["current_observation"]['temperature_string']
    time     = data["current_observation"]["observation_time"]

    tweet_output = location + '\n' + time + '\n' + temp + '\n' +"feeling like "+ wind + '\n'

    print(tweet_output)

    #api.update_status(status=tweet_output)


# ============================================================================ #
if __name__ == "__main__":
    main()
