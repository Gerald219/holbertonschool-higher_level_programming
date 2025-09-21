#!/usr/bin/python3


class Square:  # make a Square class
    """size, position, area, and to print.""" 

    def __init__(self, size=0, position=(0, 0)):  # start square with size + position
        """Set up square with size and position."""
        self.size = size  # check and save size (uses setter)
        self.position = position  # check and save position (uses setter)

    @property
    def size(self):  # getter for size
        """Return size value."""
        return self.__size  # give back hidden size

    @size.setter
    def size(self, value):  # setter for size
        """Set size with rules."""
        if not isinstance(value, int):  # must be an int
            raise TypeError("size must be an integer")  # error if not
        if value < 0:  # must not be negative
            raise ValueError("size must be >= 0")  # error if negative
        self.__size = value  # save hidden size

    @property
    def position(self):  # getter for position
        """Return position value."""
        return self.__position  # give back hidden position

    @position.setter
    def position(self, value):  # setter for position
        """Set position with rules."""
        if (  # check all rules
            not isinstance(value, tuple)  # must be a tuple
            or len(value) != 2  # must have 2 items
            or not all(isinstance(num, int) for num in value)  # both must be int
            or not all(num >= 0 for num in value)  # both must be >= 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")  # error if not
        self.__position = value  # save hidden position

    def area(self):  # method to get area
        """Return area (size * size)."""
        return self.__size * self.__size  # size times size

    def my_print(self):  # method to print square
        """Print square with # shifted by position."""
        if self.__size == 0:  # if size is 0
            print("")  # just print empty line
        else:
            # move down by position[1] (y spaces)
            for _ in range(self.__position[1]):
                print("")
            # print each row
            for _ in range(self.__size):
                # add spaces for x offset, then print #
                print(" " * self.__position[0] + "#" * self.__size)
