#!/usr/bin/python3
"""
This module introduces a new class Square that inherits from the rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle



class Square(Rectangle):
    """
    Represents a square shape.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """

        self.__size = size
        self.integer_validator("size", self.__size)
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            The string representation of the square in the format:
            [Square] <size>/<size>
        """

        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            The area of the square.
        """

        return self.__size ** 2
