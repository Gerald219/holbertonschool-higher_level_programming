#!/usr/bin/python3
"""Checks if an object is a class or inherits from one."""


def is_kind_of_class(obj, a_class):
    """Return True if its an instance or inherits from a_class."""
    return isinstance(obj, a_class)
