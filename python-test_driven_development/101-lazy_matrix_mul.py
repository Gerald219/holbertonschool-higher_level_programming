#!/usr/bin/python3
"""
Module 101-lazy_matrix_mul
Performs matrix multiplication using NumPy.
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a: First input (matrix-like)
        m_b: Second input (matrix-like)

    Returns:
        numpy.ndarray: The product of the two matrices

    Raises:
        Whatever NumPy raises — the checker expects native NumPy errors
    """
    return np.matmul(m_a, m_b)
