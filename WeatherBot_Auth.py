#!/usr/bin/env python
# encoding: utf-8


import re

import tweepy

from GetWeather_Data import *

# enter the corresponding information from your twitter application:
consumer_key = 'ftpSZnEi0f3JnoaBXtCg2BxH0'
# keep the quotes, replace this with your consumer key
consumer_secret = 'VX2zyXVqyhYGVsj5doIOho8VEjqQKPXrChENchyBKnzU1tWQVJ'
# keep the quotes, replace this with your consumer secret key
access_key = '796182382286163968-2FwcfnMsnNwvduip8Juyw9QD7N6dCFj'
# keep the quotes, replace this with your access token
access_secret = 'gfB2FXA5eho99pU8ZZ7RkxZI6vr8OXlgzE7LEfzx0d5XX'
# keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

if __name__ == "__main__":
    api_key = '3dfa9f9c19a712ac'
    data = get_weather_Data(api_key)
    location = data["current_observation"]["display_location"]["full"]
    wind = data["current_observation"]['windchill_string']
    temp = data["current_observation"]['temperature_string']
    time = data["current_observation"]["observation_time"]
    tweet_output = location + '\n' + time + '\n' + temp + '\n' +"feeling like "+ wind + "\n"

    api.update_status(status=tweet_output)
