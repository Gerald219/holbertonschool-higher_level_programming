#!/usr/bin/python3
"""locked class module"""


class LockedClass:
    """allow only first_name attribute"""
    __slots__ = ("first_name",)
