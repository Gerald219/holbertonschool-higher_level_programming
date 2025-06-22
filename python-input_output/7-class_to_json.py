#!/usr/bin/python3
"""Returns dictionary description for JSON serialization."""


def class_to_json(obj):
    """Returns the dictionary representation of a simple data structure."""
    return obj.__dict__
