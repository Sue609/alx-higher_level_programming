#!/usr/bin/python3
"""
This mode defines a class called Square.
"""


class Square:
    """
    It represents a square
    """


    def __init__(self, size=0):
        """
        It initializes a new square.
        
        Args:
            size (int): the size of the new square
        """

        self.size = size

    @property
    def size(self):
        """
        This function sets the surrent size of the square.
        """

        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the current area of the square.
        """

        return (self.__size * self.__size)

    def __eq__(self, other):
        """
        Define the equal to comparison of the square.
        """

        return self.area() == other.area()

    def __ne__(self, other):
        """
        Defines the != comparison to a square.
        """

        return self.area() != other.area()

    def __it__(self, other):
        """
        Defines the less than comparison.
        """

        return self.area() < other.area()

    def __le__(self, other):
        """
        Define the <= comparison to a square.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Define the >= comparison.
        """
        return self.area() >= other.area()
