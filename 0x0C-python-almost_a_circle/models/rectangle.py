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
        A class constructor that initializes private attributes.
        """

        super().__init__(id=id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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


if __name__ == '__main__':
    unittest.main()
