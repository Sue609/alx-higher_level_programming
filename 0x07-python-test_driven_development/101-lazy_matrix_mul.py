#!/usr/bin/python3

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    matrix_a = np.array(m_a)
    matrix_b = np.array(m_b)

    if matrix_a.shape[1] != matrix_b.shape[0]:
        raise ValueError("m_a and m_b can't be multiplied")

    result = np.dot(matrix_a, matrix_b)
    return result

if __name__ == "__main__":
    import doctest
    doctest.testfile("101-lazy_matrix_mul.txt")
