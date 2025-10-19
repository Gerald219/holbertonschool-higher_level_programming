#!/usr/bin/python3
"""Add items from the command line and save them to a JSON file."""

import sys  # to read command line arguments
import json
from os import path  # to check if file exists


filename = "add_item.json"

# if yes → open it read mode and load what's inside
if path.exists(filename):
    with open(filename, "r", encoding="utf-8") as f:
        items = json.load(f)  # turns json text into a python list
else:
    items = []  # if no file yet, start empty

# add whatever i type after the script name
# sys.argv[1:] = skip script name, take the rest
items.extend(sys.argv[1:])

# open file again
# json.dump writes & saves the list back inside as text
with open(filename, "w", encoding="utf-8") as f:
    json.dump(items, f)
