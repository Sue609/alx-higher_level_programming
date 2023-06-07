#!/usr/bin/python3
"""This module introduces the function print_square."""


def print_square(size):
    """
    Prints a square made of '#' characters with the specified size.

    Args:
        size (int): The size of the square.

    Raises:
        TypeError: If the size is not an integer.
        ValueError: If the size is less than 0.

    Returns:
        None
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
