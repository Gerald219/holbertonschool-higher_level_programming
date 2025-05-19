#!/usr/bin/python3
"""
Divides all elements of a matrix by a number.
Each result is rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """
    Returns a new matrix with each value divided by div.

    Args:
        matrix: list of lists of ints/floats
        div: number to divide by

    Raises:
        TypeError, ZeroDivisionError

    Returns:
        A new matrix
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(x, (int, float)) for row in matrix for x in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]