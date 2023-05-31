#!/usr/bin/python3
"""
Defines a MagicClass for the bytecode.
"""


import math


class MagicClass:
    """
    This class represents a circle.
    """

    def __init__(self, radius=0):
        """
        This function initializes a magic class.
        Arg:
            radius (float or int): The radius of the bytecode.
        """

    self.__radius = 0
    if type(radius) is not int and type(radius) is not float:
        raise TypeError("radius must be a number")
    self.__radius = radius

    def area(self):
        """
        Returns the area.
        """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return The circumference of the MagicClass."""
        return (2 * math.pi * self.__radius)

