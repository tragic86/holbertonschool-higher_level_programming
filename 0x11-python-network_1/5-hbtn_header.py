#!/usr/bin/python3
"""Same as tasks 1 only using requestes"""

import requests
from sys import argv


if __name__ == "__main__":

    first = requests.get(argv[1])
    print(first.headers.get('X-Request-Id'))
