#!/usr/bin/python3
"""Module that provides lazy matrix multiplication using NumPy.
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using NumPy's matmul.

    Args:
        m_a (list of lists): First matrix.
        m_b (list of lists): Second matrix.

    Returns:
        numpy.ndarray: The result of the matrix multiplication.
    """
    return np.matmul(m_a, m_b)
