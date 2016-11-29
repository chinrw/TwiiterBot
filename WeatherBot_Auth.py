#!/usr/bin/env python
# encoding: utf-8

import tweepy
from GetWeather_Data import *

# enter the corresponding information from your twitter application:
consumer_key = 'ftpSZnEi0f3JnoaBXtCg2BxH0'
# keep the quotes, replace this with your consumer key
consumer_secret = 'VX2zyXVqyhYGVsj5doIOho8VEjqQKPXrChENchyBKnzU1tWQVJ'
# keep the quotes, replace this with your consumer secret key
access_key = '796182382286163968-fc9ewRIC4gNhVRAz6ZYw0QkaDBwE2W2'
# keep the quotes, replace this with your access token
access_secret = 'QZa7h3Grix7PAVFThrsgKBa3Ic40f0wyRTSKsUGKb6m7i'
# keep the quotes, replace this with your access token secret

def authenticate(cons_key, cons_secret, acc_key, acc_secret):
    '''
    Authenticates Twitter credentials.
    Returns Twitter API object.
    '''
    auth = tweepy.OAuthHandler(cons_key, cons_secret)
    auth.set_access_token(acc_key, acc_secret)
    return tweepy.API(auth, parser=tweepy.parsers.JSONParser())

def run():
    '''
    Main function to run the program.
    '''
    api = authenticate(consumer_key, consumer_secret, access_key, access_secret)
    api_key = '3dfa9f9c19a712ac'
    data = get_weather_Data(api_key)

    location = data["current_observation"]["display_location"]["full"]
    wind     = data["current_observation"]['windchill_string']
    temp     = data["current_observation"]['temperature_string']
    time     = data["current_observation"]["observation_time"]
    tweet_output = location + '\n' + time + '\n' + temp + '\n' +"feeling like "+ wind + '\n'

    api.update_status(status=tweet_output)


if __name__ == "__main__":
    run()
