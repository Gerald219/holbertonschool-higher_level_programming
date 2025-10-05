#!/usr/bin/python3
"""action to check if an object is exactly an instance of a present class."""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class, or False."""
    return type(obj) is a_class
