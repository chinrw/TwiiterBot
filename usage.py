#!/usr/bin/env python

import sys

def usage():
    '''
    Prints usage for program.
    '''
    print("Usage: ./%s <keys.txt>"%(sys.argv[0]))
    print("    keys.txt should have only the following on each respective line:")
    print("    Line 1:    'consumer key'")
    print("    Line 2:    'consumer secret'")
    print("    Line 3:    'access key'")
    print("    Line 4:    'access secret'")
