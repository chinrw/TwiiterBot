#!/usr/bin/env python
# encoding: utf-8

import urllib2,urllib
import json

def get_weather_Data(cityid, api_key):

    headers = { #pretent to be explorer
        'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) \
        Gecko/20091201 Firefox/3.5.6'
    }

    url = 'http://api.openweathermap.org/data/2.5/forecast/city?id=%d&APPID=%s'\
        %(cityid, api_key)
    req = urllib2.Request(url,headers=headers)
    content = urllib2.urlopen(req).read()
    data = json.loads(content)

    return data

if __name__ == "__main__":
    cityid = 5141502
    api_key = 'f5e9db5f5e582a912c6dd798d63e1a1f'
    get_weather_Data(cityid, api_key)
