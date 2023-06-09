#!/usr/bin/python3
"""
We introduce a module where we define a new class.
"""
from models.base import Base


class Rectangle(Base):
    """
    A new class that inherits from the Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):

        """
        class constructor that initializes attributes.
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Getter for the width private attribute.
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter fo the height attribute.
        """

        return self.__height

    @height.setter
    def height(self, value):
       """
       Setter fo the private attribute height.
       """

       if not isinstance(value, int):
            raise TypeError("height must be an integer")
       if value <= 0:
            raise ValueError("height must be > 0")
       self.__height = value

    @property
    def x(self):
        """
        getter for private sttribute 'x'.
        """

        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for private attribute.
        """

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter for private attribute 'y'.
        """

        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for private attribute 'y'.
        """

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Method that calculates the area of a rectangle.
        """

        return self.width * self.height

    def display(self):
        """
        Prints the character '#' to the stdout.
        """

        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + '#' * self.width)

    def __str__(self):
        """
        Method that defines represention of object
        """

        return (
            f"[Rectangle] ({self.id}) {self.x}/{self.y} "
            f"- {self.width}/{self.height}"
        )

    def update(self, *args, **kwargs):
        """
        Method that updates the attributes of the Rectangle.
        Args:
            *args: No keyworded arguements
            **kwargs: Keyworded arguements rep attributes.
        """

        if args:
            attr_names = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attr_names[i], arg)
        elif kwargs:
            for attr, value in kwargs.items():
                setattr(self, attr, value)

    def to_dictionary(self):
        """
        Method to update a dictionary representation of Rectangle.
        """

        return {
                'x': self.x,
                'y': self.y,
                'id': self.id,
                'height': self.height,
                'width': self.width
            }

    def to_csv_row(self):
        """
        Converts the Rectangle object to a CSV row format.
        """

        return [self.id, self.width, self.height, self.x, self.y]

    @classmethod
    def from_csv_row(cls, row):
        """
        Creates a new Rectangle object from a CSV row.
        """

        id, width, height, x, y = map(int, row)
        return cls(width, height, x, y, id)


if __name__ == '__main__':
    unittest.main()
