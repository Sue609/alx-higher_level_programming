#!/usr/bin/python3

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_reversed_list(self):
        result = max_integer([4, 3, 2, 1])
        self.assertEqual(result, 4)

    def test_duplicate_values(self):
       result = max_integer([1, 3, 3, 2])
       self.assertEqual(result, 3)

    def test_negative_numbers(self):
        result = max_integer([-1, -5, -3, -2])
        self.assertEqual(result, -1)

    def test_large_numbers(self):
        result = max_integer([1000, 999, 10000, 500])
        self.assertEqual(result, 10000)

    def test_one_number(self):
        result = max_integer([7])
        self.assertEqual(result, 7)

    #Testing a list of floating values
    def test_float_number(self):
        result = max_integer([1.45, 15.8, 6, 10, 12])
        self.assertEqual(result, 15.8)

    #Testing a string
    def test_string(self):
        strings = ["name", "susan", "my", "is"]
        result = max_integer(strings)
        self.assertEqual(result, "susan")

    def test_empty_string(self):
        result = max_integer("")
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()

