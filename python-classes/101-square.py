#!/usr/bin/python3
"""Square class with size, position, area, print, and str."""


class Square:
    """Square with size, position, and printing."""

    def __init__(self, size=0, position=(0, 0)):
        """Start square with size and position."""
        self.size = size        # check + save size
        self.position = position  # check + save position

    @property
    def size(self):
        """Get size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size (must be int >= 0)."""
        if not isinstance(value, int):   # must be int
            raise TypeError("size must be an integer")
        if value < 0:                    # no negatives
            raise ValueError("size must be >= 0")
        self.__size = value              # save size

    @property
    def position(self):
        """Get position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position (tuple of 2 positive ints)."""
        if (
            not isinstance(value, tuple) or   # must be tuple
            len(value) != 2 or                # must be 2 items
            not all(isinstance(num, int) for num in value) or  # must be int
            not all(num >= 0 for num in value)  # must be >= 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value               # save position

    def area(self):
        """Get area (size * size)."""
        return self.__size * self.__size

    def my_print(self):
        """Print square using # and position."""
        if self.__size == 0:          # if size 0
            print("")                 # print empty
            return

        for _ in range(self.__position[1]):  # move down
            print("")
        for _ in range(self.__size):         # rows
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Return square as string (like my_print)."""
        if self.__size == 0:
            return ""   # empty string

        lines = []
        lines.extend(["" for _ in range(self.__position[1])])  # top offset
        for _ in range(self.__size):                          # each row
            line = " " * self.__position[0] + "#" * self.__size
            lines.append(line)
        return "\n".join(lines)  # return all lines
