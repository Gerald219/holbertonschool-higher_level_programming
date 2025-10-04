#!/usr/bin/python3
"""defines a function that lists attributes and methods of an object."""


def lookup(obj):
    """return the list of available attributes."""
    return dir(obj)
