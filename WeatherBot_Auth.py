#!/usr/bin/env python

import sys
import tweepy

class Authorizer(object):
    """
    Authorizer class for Twitter Authentication.
    """
    def __init__(self, filename):
        """
        Initialize Authorizer object from file from data.
        """
        self.__filename = filename
        self.__consumer_key = str()
        self.__consumer_secret = str()
        self.__access_key = str()
        self.__access_secret = str()
        self.__weather_key = str()
        self.parse_file(self.__filename)

    def parse_file(self, filename):
        """
        Parses input file for consumer/access keys/secrets.
        """
        with open(filename) as f:
            lines = f.readlines()
            keys = 0
            for line in xrange(len(lines)):
                if lines[line][0] != "#":
                    key = lines[line].rstrip()
                    keys += 1
                    if keys == 1:
                        self.__consumer_key =  key
                    elif keys == 2:
                        self.__consumer_secret = key
                    elif keys == 3:
                        self.__access_key = key
                    elif keys == 4:
                        self.__access_secret = key
                    elif keys == 5:
                        self.__weather_key = key
                    else:
                        break

    def get_cons_key(self):
        """
        Returns the Twitter consumer key.
        """
        return self.__consumer_key

    def get_cons_secret(self):
        """
        Returns the Twitter consumer secret.
        """
        return self.__consumer_secret

    def get_acc_key(self):
        """
        Returns the Twitter access key.
        """
        return self.__access_key

    def get_acc_secret(self):
        """
        Returns the Twitter access secret.
        """
        return self.__access_secret

    def get_weather_key(self):
        """
        Returns the WUnderground API key.
        """
        return self.__weather_key

def authenticate(keys_file):
    """
    Authenticates app with Twitter.
    Returns API object and Weather key
    """
    auth = Authorizer(keys_file)
    auth_handler = tweepy.OAuthHandler(auth.get_cons_key(), auth.get_cons_secret())
    auth_handler.set_access_token(auth.get_acc_key(), auth.get_acc_secret())
    return tweepy.API(auth_handler, parser=tweepy.parsers.JSONParser()),\
            auth_handler,auth.get_weather_key()


def run():
    """
    Main function for testing.
    """
    if len(sys.argv) < 2:
        print ("Error: Not enough arguments.")
        from usage import usage
        usage()
        sys.exit(1)

    authenticate(sys.argv[1])

# ============================================================================ #
if __name__ == "__main__":
    run()
