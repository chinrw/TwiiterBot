#!/usr/bin/env python
# encoding: utf-8


import tweepy
import re


#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'ftpSZnEi0f3JnoaBXtCg2BxH0'
#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'VX2zyXVqyhYGVsj5doIOho8VEjqQKPXrChENchyBKnzU1tWQVJ'
#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '796182382286163968-2FwcfnMsnNwvduip8Juyw9QD7N6dCFj'
#keep the quotes, replace this with your access token
ACCESS_SECRET = 'gfB2FXA5eho99pU8ZZ7RkxZI6vr8OXlgzE7LEfzx0d5XX'
#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)


api = tweepy.API(auth)
highpoints = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
public_tweets = api.home_timeline()
word = "just a test"
api.update_status(status = word)
