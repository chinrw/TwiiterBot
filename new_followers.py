#!/usr/bin/env python
# encoding: utf-8
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


if __name__ == "__main__":

    arg_check()

    keys_file = sys.argv[1]
    twitter, auth, weather_key = authenticate(keys_file)
