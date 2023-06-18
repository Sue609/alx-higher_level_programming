#!/usr/bin/pyhton3

import unittest

from models.square import Square

class TestSquareClass(unittest.TestCase):
    def test_constructor(self):
        square = Square(5, 2, 3, 1)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)

    def test_size_property(self):
        square = Square(5)
        square.size = 10
        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)

    def test_str_method(self):
        square = Square(5, 2, 3, 1)
        self.assertEqual(str(square), "[Square] (1) 2/3 - 5")


    def test_setter_and_getter(self):
        square = Square(5)
        square.size = 8
        self.assertEqual(square.size, 8)

    def test_update_method(self):
        square = Square(5, 2, 3, 1)
        square.update(10, 6, 6, 2)
        self.assertEqual(square.id, 10)
        self.assertEqual(square.size, 6)
        self.assertEqual(square.width, 6)
        self.assertEqual(square.height, 6)
        self.assertEqual(square.x, 6)
        self.assertEqual(square.y, 2)

    def test_update_with_args(self):
        square = Square(5, 2, 3, 1)
        square.update(15, 8, 10, 3)
        self.assertEqual(square.id, 15)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.x, 10)
        self.assertEqual(square.y, 3)

    def test_update_with_kwargs(self):
        square = Square(5, 2, 3, 1)
        square.update(id=15, size=8, x=10, y=3)
        self.assertEqual(square.id, 15)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.x, 10)
        self.assertEqual(square.y, 3)

    def test_update_with_args_and_kwargs(self):
        square = Square(5, 2, 3, 1)
        square.update(15, 8, 10, 3, size=20, color='blue')
        self.assertEqual(square.id, 15)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.x, 10)
        self.assertEqual(square.y, 3)

    def test_update_with_empty_args_and_kwargs(self):
        square = Square(5, 2, 3, 1)
        square.update()
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_to_dictionary_method(self):
        square = Square(5, 2, 3, 1)
        dictionary = square.to_dictionary()
        expected_dict = {
                'id': 1,
                'size': 5,
                'x': 2,
                'y': 3
            }
        self.assertEqual(dictionary, expected_dict)
        self.assertIsInstance(dictionary, dict)

    def test_default_initialization(self):
        square = Square(5)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)
        self.assertEqual(square.id, 32)

    def test_update_with_positional_arguments(self):
        square = Square(5)
        square.update(2, 10, 3, 2)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 2)

    def test_update_with_keyword_arguments(self):
        square = Square(5)
        square.update(size=10, y=3, x=2, id=2)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_to_dictionary_after_updates(self):
        square = Square(5, 2, 3, 1)
        square.update(size=10, y=4)
        dictionary = square.to_dictionary()
        expected_dict = {
                'id': 1,
                'size': 10,
                'x': 2,
                'y': 4
            }
        self.assertEqual(dictionary, expected_dict)

    def test_str_representation(self):
        square = Square(5, 2, 3, 1)
        expected_str = "[Square] (1) 2/3 - 5"
        self.assertEqual(str(square), expected_str)

    def test_create_square(self):
        square_dict = {'id': 2, 'size': 4, 'x': 0, 'y': 0}
        square = Square.create(**square_dict)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 4)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)


if __name__ == '__main__':
    unittest.main()
