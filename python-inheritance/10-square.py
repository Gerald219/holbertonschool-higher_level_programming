#!/usr/bin/python3
"""Square class that inherits from Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square using Rectangles tools"""

    def __init__(self, size):
        # check that size is a valid integer
        self.integer_validator("size", size)
        # store size as private
        self.__size = size
        # call Rectangle’s __init__ with width = height = size
        super().__init__(size, size)
