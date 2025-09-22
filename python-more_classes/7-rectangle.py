#!/usr/bin/python3
"""Rectangle class with customizable print symbol."""


class Rectangle:
    """Rectangle with width, height, counter, and custom symbol."""

    number_of_instances = 0  # how many rectangles exist now?
    print_symbol = "#"  # symbol used to draw the rectangle

    def __init__(self, width=0, height=0):
        self.width = width  # set width
        self.height = height  # set height
        Rectangle.number_of_instances += 1  # add 1, count

    @property
    def width(self):
        return self.__width  # return the width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):  # width must be a number
            raise TypeError("width must be an integer")
        if value < 0:  # width must be zero or more
            raise ValueError("width must be >= 0")
        self.__width = value  # save the width

    @property
    def height(self):
        return self.__height  # return height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):  # height must be a number
            raise TypeError("height must be an integer")
        if value < 0:  # height must be zero or more
            raise ValueError("height must be >= 0")
        self.__height = value  # save the height

    def area(self):
        return self.__width * self.__height  # width × height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0  # no perimeter if flat
        return 2 * (self.__width + self.__height)  # add all sides

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""  # empty string if no size
        # draw rows with print_symbol, width long, repeat for height
        return "\n".join(str(self.print_symbol) * self.__width
                         for _ in range(self.__height))

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"
        # text to recreate the rectangle

    def __del__(self):
        Rectangle.number_of_instances -= 1  # eliminate 1 when deleted
        print("Bye rectangle...")  # goodbye message
