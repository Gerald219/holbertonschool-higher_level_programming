#!/usr/bin/python3
"""Converts a JSON string back into a Python object."""


import json


def from_json_string(my_str):
    """Takes a JSON string and returns the string in python object mode."""
    return json.loads(my_str)
