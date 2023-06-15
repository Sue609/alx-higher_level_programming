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

    def test_string_height(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

    def test_string_width(self):
        with self.assertRaises(TypeError):
            Rectangle("2", 10)

    def test_width_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_height_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(2, 0)

    def test_negative_x(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -1, 0)

    def test_negative_width(self):
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            Rectangle(2, -10)

    def test_negative_y(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 1, -1)

    def test_area(self):
        rectangle = Rectangle(2, 3)
        self.assertEqual(rectangle.area(), 6)

    def test_area_with_other_elements(self):
        rectangle = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(rectangle.area(), 56)

if __name__ == '__main__':
    unittest.main()
