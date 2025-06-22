#!/usr/bin/python3
"""Defines a function that returns Pascal’s Triangle up to n rows."""


def pascal_triangle(n):
    """Generate Pascal’s Triangle with n rows.

    Returns:
        A list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev = triangle[-1]
        row = [1]
        for j in range(1, i):
            row.append(prev[j - 1] + prev[j])
        row.append(1)
        triangle.append(row)

    return triangle
