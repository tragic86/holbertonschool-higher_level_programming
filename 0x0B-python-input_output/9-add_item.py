#!/usr/bin/python3


import sys

load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

add = "add_item.json"
argv = sys.argv[1:]

try:
    i = load_from_json_file(add)
    save_to_json_file(i + argv, add)
except Exception:

    save_to_json_file(argv, add)
