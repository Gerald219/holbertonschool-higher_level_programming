#!/usr/bin/python3
"""This module loads data from a JSON file and returns the corresponding object."""

import json


def load_from_json_file(filename):
    """Load a Python object from a JSON file."""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
