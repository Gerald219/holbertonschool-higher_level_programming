#!/usr/bin/python3
"""Defines a function that returns available attributes and methods."""


def lookup(obj):
    """Returns a list of attributes and methods of the object."""
    return dir(obj)
