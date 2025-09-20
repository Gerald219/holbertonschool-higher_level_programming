#!/usr/bin/python3

"""Square module with print method."""

class Square:  # make a Square class
    """Square with size check, area, and print."""

    def __init__(self, size=0):  # start square with size (default 0)
        """Set up square with size."""
        self.size = size  # send value to setter for checks

    @property
    def size(self):  # getter for size
        """Return size value."""
        return self.__size  # give back hidden size

    @size.setter
    def size(self, value):  # setter for size
        """Set size with rules."""
        if not isinstance(value, int):  # if not an int
            raise TypeError("size must be an integer")  # error
        if value < 0:  # if negative
            raise ValueError("size must be >= 0")  # error
        self.__size = value  # save hidden size

    def area(self):  # method to get area
        """Return area (size * size)."""  # method note
        return self.__size * self.__size  # size times size

    def my_print(self):
        """Print square with # or empty line if size is 0."""
        if self.__size == 0:  # if size is 0
            print("")  # just print empty line
        else:
            for _ in range(self.__size):  # repeat for each row
                print("#" * self.__size)  # row = size number of #
