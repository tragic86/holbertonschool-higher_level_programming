#!/usr/bin/python3
"""take an url and email"""

import urllib.request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values).encode('utf-8')
    req = urllib.request.Request(values, data)
    with urllib.request.urlopen(argv[1], data) as response:
        print(response.read().decode('utf-8'))
