#!/usr/bin/python3
"""Function that multiplies 2 matrices using NumPy"""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using numpy.matmul"""
    return np.matmul(m_a, m_b)
