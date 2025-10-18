#!/usr/bin/python3
"""Load data from a JSON file into a Python object."""

import json


def load_from_json_file(filename):
    """Open a JSON file and get the data back as Python."""

    # open the file in read mode
    with open(filename, "r", encoding="utf-8") as f:
        # read the json text inside and turn it back into python data
        return json.load(f)
