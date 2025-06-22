#!/usr/bin/python3
"""Module 6-load_from_json_file
Defines load_from_json_file function
"""

import json


def load_from_json_file(filename):
    """Reads JSON content from a file and returns the Python object"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
