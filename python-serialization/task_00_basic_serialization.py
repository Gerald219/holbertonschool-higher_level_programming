#!/usr/bin/env python3
"""serialization and deserialization using JSON in Python."""

import json  # Import the JSON module


def serialize_and_save_to_file(data, filename):
    """function sets up the data, and location to save the JSON file."""

    with open(filename, "w", encoding="utf-8") as f:
        # open file, write with w mode
        # using utf-8 to save letters and symbols correctly
        json.dump(data, f)
        # dump data to file f as plain JSON text


def load_and_deserialize(filename):
    """reads the JSON file and deserializes the content back into object."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
        # load data from file f and return the deserialized object
