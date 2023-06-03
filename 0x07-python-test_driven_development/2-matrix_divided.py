#!/usr/bin/python3

def matrix_divided(matrix, div):
    if not all(isinstance(row, list) and all(isinstance(val, (int, float)) for val in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")


    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")


    if div == 0:
        raise ZeroDivisionError("division by zero")


    divided_matrix = [[round(val / div, 2) for val in row] for row in matrix]

    return (divided_matrix)

if __name__ == "__main__":
    import doctest
    doctest.testfile("2-matrix_divided.txt")

