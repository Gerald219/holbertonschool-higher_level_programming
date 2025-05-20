#!/usr/bin/python3
"""Defines Square with getter, setter, and area."""


class Square:
    """Square with size validation, getter, setter, and area."""

    def __init__(self, size=0):
        self.size = size  # uses the setter logic

    @property
    def size(self):
        return self.__size  # returns the current size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):  # make sure it's an int
            raise TypeError("size must be an integer")
        if value < 0:  # make sure it's >= 0
            raise ValueError("size must be >= 0")
        self.__size = value  # save it privately

    def area(self):
        return self.__size * self.__size
