#!/usr/bin/env python

import sys
import tweepy

class Authorizer(object):
    '''
    Authorizer class for Twitter Authentication.
    '''
    def __init__(self, filename):
        '''
        Initialize Authorizer object from file from data.
        '''
        self.__filename = filename
        self.__consumer_key = str()
        self.__consumer_secret = str()
        self.__access_key = str()
        self.__access_secret = str()
        self.parse_file(self.__filename)

    def parse_file(self, filename):
        '''
        Parses input file for consumer/access keys/secrets.
        '''
        with open(filename) as f:
            lines = f.readlines()
            keys = 0
            for line in xrange(len(lines)):
                if lines[line][0] != "#":
                    key = lines[line].rstrip()
                    keys += 1
                    if keys == 1:
                        self.consumer_key =  key
                    elif keys == 2:
                        self.consumer_secret = key
                    elif keys == 3:
                        self.access_key = key
                    elif keys == 4:
                        self.access_secret = key
                    else:
                        break

    def get_cons_key(self):
        '''
        Returns the consumer key.
        '''
        return self.__consumer_key

    def get_cons_secret(self):
        '''
        Returns the consumer secret.
        '''
        return self.__consumer_secret

    def get_acc_key(self):
        '''
        Returns the access key.
        '''
        return self.__access_key

    def get_acc_secret(self):
        '''
        Returns the access secret.
        '''
        return self.__access_secret

def authenticate(keys_file):
    '''
    Authenticates app with Twitter.
    Returns API object.
    '''
    auth = Authorizer(keys_file)
    auth_handler = tweepy.OAuthHandler(auth.get_cons_key(), auth.get_cons_secret())
    auth_handler.set_access_token(auth.get_acc_key(), auth.get_acc_secret())
    return tweepy.API(auth_handler, parser=tweepy.parsers.JSONParser())

def run():
    '''
    Main function for testing.
    '''
    if len(sys.argv) < 2:
        print ("Error: Not enough arguments.")
        from usage import usage
        usage()
        sys.exit(1)

    authenticate(sys.argv[1])

# ============================================================================ #
if __name__ == "__main__":
    run()
