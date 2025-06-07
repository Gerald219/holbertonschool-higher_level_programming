#!/usr/bin/python3
"""Defines a function to check class inheritance."""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance or inherits from a_class."""
    return isinstance(obj, a_class)
