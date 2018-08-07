#!/usr/bin/python3
"""Script to get error code"""

import urllib.request
from sys import argv


if __name__ == "__main__":

    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as req:
            print(req.read().decode('utf-8'))

    except urllib.error.HTTPError as bad:
        print("Error code: {}".format(bad.code))
