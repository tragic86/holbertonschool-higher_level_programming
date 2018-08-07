#!/usr/bin/python3
"""script for url and email addy"""

import requests
from sys import argv


if __name__ == "__main__":
    values = {'email': argv[2]}
    temp = request.post(argv[1], data=values)
    print(temp.text)
