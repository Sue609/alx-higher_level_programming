#!/usr/bin/python3
"""
This module introduces a function.
"""


def pascal_triangle(n):
    """
    Function that returns list of integers.
    Args:
        n: an integer
    Return:
        empty list if n <= 0
    """

    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        prev_row = triangle[i - 1]

        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)
        triangle.append(row)
    return triangle
