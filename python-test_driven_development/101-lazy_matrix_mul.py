#!/usr/bin/python3
"""
This module provides a function to multiply two matrices using NumPy.
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy.

    Args:
        m_a (list of lists): First matrix with integers/floats.
        m_b (list of lists): Second matrix with integers/floats.

    Returns:
        numpy.ndarray: The product of the two matrices.

    Raises:
        ValueError: If the matrices cannot be multiplied.
        TypeError: If inputs are not lists of lists of numbers.
    """
    return np.matmul(m_a, m_b)
