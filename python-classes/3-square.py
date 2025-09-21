#!/usr/bin/python3

"""Square module that checks size and gets area."""


class Square:
    """Square with size check and area."""

    def __init__(self, size=0):  # start square with size default is 0
        """Set up square with size."""
        if not isinstance(size, int):  # if size is not a number
            raise TypeError("size must be an integer")  # stop: must be int
        if size < 0:  # if size is negative
            raise ValueError("size must be >= 0")  # stop must be 0 or more
        self.__size = size  # keep the size hidden inside

    def area(self):  # get area of square
        """Return area (size * size)."""
        return self.__size * self.__size  # size times size
