#!/usr/bin/python3
"""Returns the dictionary description of a simple data structure."""


def class_to_json(obj):
    """Return the __dict__ of an object for JSON serialization."""
    return obj.__dict__
