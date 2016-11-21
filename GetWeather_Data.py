#!/usr/bin/env python
# encoding: utf-8

import urllib2,urllib
import json

def get_weather_Data(cityid, api_key):
    # return a dict data that coutains required information

    url = 'http://api.wunderground.com/api/%s/hourly/q/NY/Troy.json'\
        %(api_key)
    req = urllib2.Request(url)
    content = urllib2.urlopen(req).read()
    data = json.loads(content)

    return data

if __name__ == "__main__":
    cityid = 5141502
    api_key = '3dfa9f9c19a712ac'
    get_weather_Data(cityid, api_key)
