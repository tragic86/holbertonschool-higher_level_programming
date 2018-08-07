#!/usr/bin/python3
"""Python script using request"""


import requests


if __name__ == "__main__":
    reqs = requests.get('https://intranet.hbtn.io/status')

    print("Body response:")
    print("\t- type: {}".format(type(reqs.text)))
    print("\t- content: {}".format(reqs.text))
