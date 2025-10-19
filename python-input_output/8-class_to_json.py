#!/usr/bin/python3
"""Turn a class instance into a simple dictionary."""

def class_to_json(obj):
    """dictionary with all readable attributes of an object."""
    return obj.__dict__
