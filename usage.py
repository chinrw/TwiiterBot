#!/usr/bin/env python

import sys

def usage():
    '''
    Prints usage for program.
    '''
    print("Usage: ./%s <keys.txt> <minutes>"%(sys.argv[0]))
    print("    keys.txt should have only the following on each respective line:")
    print("    Line 1:    'Twitter consumer key'")
    print("    Line 2:    'Twitter consumer secret'")
    print("    Line 3:    'Twitter access key'")
    print("    Line 4:    'Twitter access secret'")
    print("    Line 5:    'WUnderground API key'")
    print(" ")
    print("    minutes  -  Tweet interval in minutes, must be >15")
