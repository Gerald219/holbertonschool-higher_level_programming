#!/usr/bin/python3
"""Save a Python object into a file in JSON format."""

import json


def save_to_json_file(my_obj, filename):
    """Save the given data inside the file."""
    # open or create the file
    with open(filename, "w", encoding="utf-8") as f:
        # write the data in json form into the file
        json.dump(my_obj, f)
