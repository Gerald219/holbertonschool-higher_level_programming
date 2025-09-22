#!/usr/bin/python3
"""Rectangle with width, height, area and perimeter."""


class Rectangle:
    """Rectangle with width and height."""

    def __init__(self, width=0, height=0):
        self.width = width  # set the starting width
        self.height = height  # set the starting height

    @property
    def width(self):
        return self.__width  # give back the width when asked

    @width.setter
    def width(self, value):
        if not isinstance(value, int):  # only whole numbers allowed
            raise TypeError("width must be an integer")
        if value < 0:  # width cannot be negative
            raise ValueError("width must be >= 0")
        self.__width = value  # store the width safely

    @property
    def height(self):
        return self.__height  # give back the height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):  # only whole numbers allowed
            raise TypeError("height must be an integer")
        if value < 0:  # height cannot be negative
            raise ValueError("height must be >= 0")
        self.__height = value  # store the height

    def area(self):
        return self.__width * self.__height  # multiply width × height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0  # no perimeter if flat line
        return 2 * (self.__width + self.__height)  # add all 4 sides together
