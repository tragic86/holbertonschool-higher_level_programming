#!/usr/bin/python3
""" script to get request"""

import urllib.request
with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
    code = html.decode('UTF-8')

    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- uft8 content: {}".format(code))
