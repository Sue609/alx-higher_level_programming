#!/usr/bin/python3
"""
This module introduces a class that inherits from Rectangle.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A new class function that inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        A class constructor that initializes attributes.
        Args:
            size (int): Size of the square.
            x (int): x-coordinate of the square's position (default: 0).
            y (int): y-coordinate of the square's position (default: 0).
            id (int): Identifier of the square (default: None).
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the square instance.
        """

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
        Adding the public getter and setter size.
        """

        return self.width

    @size.setter
    def size(self, value):
        """
        Adding a setter to the method.
        """

        self.width = value
        self.height = value

if __name__ == '__main__':
    unittest.main()
