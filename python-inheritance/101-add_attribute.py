#!/usr/bin/python3
"""adds a new attribute if possible."""


def add_attribute(obj, name, value):
    """Add a new attribute to object if allowed."""
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
