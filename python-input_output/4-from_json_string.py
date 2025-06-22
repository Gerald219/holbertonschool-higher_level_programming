#!/usr/bin/python3
"""Converts a JSON string back into a Python object."""

import json


def from_json_string(my_str):
    """Returns the Python object from a JSON string."""
    return json.loads(my_str)
