#!/usr/bin/python3
"""
2-matrix_divided module
Defines function to divide all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by div, rounded to 2 decimals.

    Args:
        matrix: list of lists of ints/floats.
        div: int or float, divisor.

    Returns:
        New matrix with elements divided by div.

    Raises:
        TypeError: if matrix is not a list of lists of numbers,
                   or if rows differ in size,
                   or if div is not a number.
        ZeroDivisionError: if div is 0.
    """
    # validate matrix
    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(x, (int, float)) for row in matrix for x in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # validate row sizes
    row_length = len(matrix[0])
    if any(len(row) != row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # validate divisor
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]
