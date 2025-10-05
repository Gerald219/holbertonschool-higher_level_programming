#!/usr/bin/python3
"""Check if an object comes from a child class."""


def inherits_from(obj, a_class):
    """True when object class inherits from a_class."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
