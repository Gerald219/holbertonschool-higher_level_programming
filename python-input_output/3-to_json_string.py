#!/usr/bin/python3
"""Converts a Python object into a JSON string."""


import json


def to_json_string(my_obj):
    """Takes object and returns its json string form, to be read."""
    return json.dumps(my_obj)
