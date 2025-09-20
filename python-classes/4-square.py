#!/usr/bin/python3

"""Square module with getter and setter for size."""

class Square:  # make a Square class
    """Square with private size, validation, and area method."""

    def __init__(self, size=0):  # start square with size is default 0
        """Initialize square with size (default 0)."""
        self.size = size  # set size - uses setter below

    @property
    def size(self):  # getter for size
        """Return the size value."""
        return self.__size  # give back hidden size

    @size.setter
    def size(self, value):  # setter for size
        """Set size with checks."""
        if not isinstance(value, int):  # if not a number
            raise TypeError("size must be an integer")  # stop: must be int
        if value < 0:  # if negative
            raise ValueError("size must be >= 0")  # stop: must be 0 or more
        self.__size = value  # save hidden size

    def area(self):  # method to find area
        """Return area (size * size)."""
        return self.__size * self.__size  # size times size
