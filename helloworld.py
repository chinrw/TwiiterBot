#!/usr/bin/env python
# encoding: utf-8


#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys

argfile = str(sys.argv[1])

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'uUMUkkpfX5UVdZfWaiJSW5ZTZ'
#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = '38HfvjKXzDaBfPusjjGdefWmXI01ZXwjo2Er3txZtyR1il8i45'
#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '3198328536-MfZV85Q3DYokksNEAYrLR4lGnAs2h60MfuD5sit'
#keep the quotes, replace this with your access token
ACCESS_SECRET = 'jFy2f72bfLNcW8zKmVeuCu5blsu2OoJ7moT3RXHpxUedn'
#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open(argfile,'r')
f=filename.readlines()
filename.close()

for line in f:
    api.update_status(line)
    time.sleep(900)#Tweet every 15 minutes
