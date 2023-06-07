#!/usr/bin/python3
"""This isa module that defines a function.
"""

def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The divisor.

    Returns:
        list of lists: The divided matrix.

    Raises:
        TypeError: If matrix is not a list of lists,
        contains non-numeric values, or rows of different lengths.
    """

    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    divided_matrix = [[round(val / div, 2) for val in row] for row in matrix]

    return divided_matrix
