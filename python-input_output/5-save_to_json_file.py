#!/usr/bin/python3
"""Save object to a file using JSON format."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON format."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
