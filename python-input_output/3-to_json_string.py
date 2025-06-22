#!/usr/bin/python3
"""This module defines a function to convert objects to JSON strings."""


import json


def to_json_string(my_obj):
    """Returns the JSON string representation of an object."""
    return json.dumps(my_obj)
