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

    def update(self, *args, **kwargs):
        """
        Updating the class by adding public method.
        """

        if args:
            attribute = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attribute[i], arg)
        else:
            for attr, value in kwargs.items():
                setattr(self, attr, value)

    def to_dictionary(self):
        """
        Method to update the class square to a dictionary.
        """

        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
            }

    def to_csv_row(self):
        """
        Converts the Square object to a CSV row format.
        """

        return [self.id, self.size, self.x, self.y]

    @classmethod
    def from_csv_row(cls, row):
        """
        Creates a new Square object from a CSV row.
        """

        id, size, x, y = map(int, row)
        return cls(size, x, y, id)


if __name__ == '__main__':
    unittest.main()
