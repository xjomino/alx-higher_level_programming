#!/usr/bin/python3
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    try:
        return np.matmul(m_a, m_b)
    except ValueError as e:
        if "matmul" in str(e):
            raise ValueError("matrix multiplication is not possible due to incompatible dimensions")
        else:
            raise e

