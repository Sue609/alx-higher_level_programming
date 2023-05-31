#!/usr/bin/python3
"""
This module defines the Square class.
"""


class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class with the given size.

        Args:
            size (int): The size of the square (default 0)

        """
        if not isinstance(size, int):
            raise ValueError("size must be an integer")

        elif size < 0:
            raise TypeError("size must be >= 0")
        self.__size = size


