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

        super().__init__(id)
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

        self.__y = value


if __name__ == '__main__':
    unittest.main()
