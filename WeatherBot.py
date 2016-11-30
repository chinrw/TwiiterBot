#!/usr/bin/env python

import sys
from WeatherBot_Auth import authenticate

def arg_check():
    '''
    Checks to see if enough arguments are passed to the program.
    '''
    if len(sys.argv) < 2:
        print("Error: Not enough arguments.")
        from usage import usage
        usage()
        sys.exit(1)

def main():
    '''
    Main function for WeatherBot.
    '''
    arg_check()

    keys_file = sys.argv[1]
    api = authenticate(keys_file)

    '''
    api_key = '3dfa9f9c19a712ac'
    data = get_weather_Data(api_key)

    location = data["current_observation"]["display_location"]["full"]
    wind     = data["current_observation"]['windchill_string']
    temp     = data["current_observation"]['temperature_string']
    time     = data["current_observation"]["observation_time"]

    tweet_output = location + '\n' + time + '\n' + temp + '\n' +"feeling like "+ wind + '\n'

    api.update_status(status=tweet_output)
    '''

# ============================================================================ #
if __name__ == "__main__":
    main()
