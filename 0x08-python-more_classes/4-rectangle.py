#!/usr/bin/python3
"""Define a Rectangle class."""


class Rectangle:
    """This class represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes a rectangle with the given width and weight.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Getting the width of the rectatngle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("heigth must be an integer")
        if value < 0:
            raise ValueError("heigth must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the peremeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle_str = ""
        for _ in range(self.height):
            rectangle_str += "#" * self.width + "\n"
        return rectangle_str[:-1]

    def __repr__(self):
        """should return a string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)
