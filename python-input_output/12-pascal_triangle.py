#!/usr/bin/python3
"""Function that returns Pascals triangle up to n rows."""


def pascal_triangle(n):
    """Return a list of lists representing Pascals triangle of n."""
    triangle = []  # holds all rows

    # if n is zero or less, return empty list
    if n <= 0:
        return triangle

    # first row always starts with 1
    triangle = [[1]]

    # build each next row
    for i in range(1, n):
        prev = triangle[-1]          # last row made
        new = [1]                    # every row starts with 1
        # fill middle numbers by adding two above
        for j in range(len(prev) - 1):
            new.append(prev[j] + prev[j + 1])
        new.append(1)                # every row ends with 1
        triangle.append(new)         # add new row to triangle

    return triangle
