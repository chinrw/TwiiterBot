#!/usr/bin/env python

import json
import urllib
import urllib2
from pprint import pprint


def get_weather_data(api_key, request_type, location):
    # return a dict data that coutains required information

    url = 'http://api.wunderground.com/api/%s/%s/%s.json'\
        % (api_key, request_type,location)
    req = urllib2.Request(url)
    content = urllib2.urlopen(req).read()
    data = json.loads(content)

    return data

def location_autocomplete(input):
    """
    return a series of candidates output or return "can't find this place"
    """
    url = 'http://autocomplete.wunderground.com/aq?query=%s' %(input)
    req = urllib2.Request(url)
    content = urllib2.urlopen(req).read()
    data = json.loads(content)

    return data

if __name__ == "__main__":
    cityid = 5141502
    location = '/q/zmw:12180.1.99999'
    #print get_weather_data(api_key, "conditions",location)
    pprint(location_autocomplete("troy"))
