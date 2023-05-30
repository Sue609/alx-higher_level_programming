#!/bin/python3

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

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less then 0.
        """
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")

        else:
            raise TypeError("size must be an integer")
        self.__size = size

