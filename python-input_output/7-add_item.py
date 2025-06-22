#!/usr/bin/python3
"""Adds command-line items to a list and saves to a file using JSON"""
import sys
import os.path
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

if os.path.exists(filename):
    try:
        items = load_from_json_file(filename)
    except Exception:
        items = []
else:
    items = []

items.extend(sys.argv[1:])
save_to_json_file(items, filename)
