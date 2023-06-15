#!/usr/bin/python3

import unittest

from models.rectangle import Rectangle

class TestRectangleClass(unittest.TestCase):
    def test_id_values(self):
        rectangle = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(rectangle.id, 12)

    def test_width(self):
        rectangle = Rectangle(10, 2)
        self.assertEqual(rectangle.width, 10)

    def test_height(self):
        rectangle = Rectangle(10, 2)
        self.assertEqual(rectangle.height, 2)

    def test_x(self):
        rectangle = Rectangle(10, 2, 5, 3)
        self.assertEqual(rectangle.x, 5)

    def test_y(self):
        rectangle = Rectangle(10, 2, 5, 3)
        self.assertEqual(rectangle.y, 3)

    def test_set_width(self):
        rectangle = Rectangle(10, 2)
        rectangle.width = 5
        self.assertEqual(rectangle.width, 5)

    def test_set_height(self):
        rectangle = Rectangle(10, 2)
        rectangle.height = 20
        self.assertEqual(rectangle.height, 20)

    def test_set_x(self):
        rectangle = Rectangle(10, 2, 5, 3)
        rectangle.x = 7
        self.assertEqual(rectangle.x, 7)

    def test_set_y(self):
        rectangle = Rectangle(10, 2, 5, 3)
        rectangle.y = 4
        self.assertEqual(rectangle.y, 4)


if __name__ == '__main__':
    unittest.main()
