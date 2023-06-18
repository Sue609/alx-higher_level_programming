#!/usr/bin/python3

import unittest

from models.rectangle import Rectangle

from unittest.mock import patch

import io

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

    def test_display(self):
        rectangle = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            rectangle.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_display_large_rectangle(self):
        rectangle = Rectangle(10, 5)
        expected_output = "##########\n##########\n##########\n##########\n##########\n"
        with patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            rectangle.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_display_square(self):
        rectangle = Rectangle(5, 5)
        expected_output = "#####\n#####\n#####\n#####\n#####\n"
        with patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            rectangle.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_display_different_dimensions(self):
        rectangle = Rectangle(4, 3)
        expected_output = "####\n####\n####\n"
        with patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            rectangle.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_str_format_with_id(self):
        rectangle = Rectangle(4, 6, 2, 1, 12)
        expected_output = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(str(rectangle), expected_output)

    def test_str_format_without_id(self):
        rectangle = Rectangle(5, 5, 1)
        expected_output = "[Rectangle] (20) 1/0 - 5/5"
        self.assertEqual(str(rectangle), expected_output)

    def test_str_format_with_large_numbers(self):
        rectangle = Rectangle(99, 99, 99, 99, 99)
        expected_output = "[Rectangle] (99) 99/99 - 99/99"
        self.assertEqual(str(rectangle), expected_output)

    def test_update_with_arguements(self):
        rectangle = Rectangle(4, 6, 2, 1, 12)
        rectangle.update(15, 8, 10, 3, 5)
        self.assertEqual(rectangle.id, 15)
        self.assertEqual(rectangle.width, 8)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 5)

    def test_update_with_partial_arguements(self):
        rectangle = Rectangle(4, 6, 2, 1, 12)
        rectangle.update(15, 8)
        self.assertEqual(rectangle.id, 15)
        self.assertEqual(rectangle.width, 8)
        self.assertEqual(rectangle.height, 6)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 1)

    def test_update_with_no_arguments(self):
        rectangle = Rectangle(4, 6, 2, 1, 12)
        rectangle.update()
        self.assertEqual(rectangle.id, 12)
        self.assertEqual(rectangle.width, 4)
        self.assertEqual(rectangle.height, 6)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 1)

    def test_update_with_insufficient_arguments(self):
        rectangle = Rectangle(4, 6, 2, 1, 12)
        rectangle.update(15, 8, 10)
        self.assertEqual(rectangle.id, 15)
        self.assertEqual(rectangle.width, 8)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 1)

    def test_to_dictionary(self):
        rectangle = Rectangle(10, 2, 1, 9)

        dictionary = rectangle.to_dictionary()

        self.assertEqual(dictionary['x'], rectangle.x)
        self.assertEqual(dictionary['y'], rectangle.y)
        self.assertEqual(dictionary['id'], rectangle.id)
        self.assertEqual(dictionary['height'], rectangle.height)
        self.assertEqual(dictionary['width'], rectangle.width)

    def test_test_to_dictionary_update(self):
        rectangle = Rectangle(10, 2, 1, 9)
        dictionary = rectangle.to_dictionary()
        rectangle.update(**dictionary)
        self.assertEqual(rectangle.id, dictionary['id'])
        self.assertEqual(rectangle.width, dictionary['width'])
        self.assertEqual(rectangle.height, dictionary['height'])
        self.assertEqual(rectangle.x, dictionary['x'])
        self.assertEqual(rectangle.y, dictionary['y'])

    def test_to_dictionary_empty_rectangle(self):
        rectangle = Rectangle(1, 1, 1, 1)
        dictionary = rectangle.to_dictionary()
        expected = {'id': 25, 'width': 1, 'height': 1, 'x': 1, 'y': 1}
        self.assertEqual(dictionary, expected)

    def test_to_dictionary_2(self):
        rectangle = Rectangle(4, 6, 2, 1, 12)
        dictionary = rectangle.to_dictionary()
        self.assertIsInstance(dictionary, dict)
        self.assertCountEqual(dictionary.keys(), ['id', 'width', 'height', 'x', 'y'])
        self.assertEqual(dictionary['id'], 12)
        self.assertEqual(dictionary['width'], 4)
        self.assertEqual(dictionary['height'], 6)
        self.assertEqual(dictionary['x'], 2)
        self.assertEqual(dictionary['y'], 1)

    def test_to_dictionary_after_update(self):
        rectangle = Rectangle(4, 6, 2, 1, 12)
        rectangle.update(15, 8, 10, 3, 5)
        dictionary = rectangle.to_dictionary()

    def test_save_none_to_file(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            contents = file.read()
            expected = '[]'
            self.assertEqual(contents, expected)

    def test_from_json_string_empty_string(self):
        json_string = ""
        expected_output = []
        result = Rectangle.from_json_string(json_string)
        self.assertEqual(result, expected_output)

    def test_from_json_string_none(self):
        json_string = None
        expected_output = []
        result = Rectangle.from_json_string(json_string)
        self.assertEqual(result, expected_output)

    def test_from_json_string_valid_json(self):
        json_string = '[{"height": 4, "width": 10, "id": 89}, {"height": 7, "width": 1, "id": 7}]'
        expected_output = [{"height": 4, "width": 10, "id": 89}, {"height": 7, "width": 1, "id": 7}]
        result = Rectangle.from_json_string(json_string)
        self.assertEqual(result, expected_output)

    def test_from_json_string_empty_list(self):
        json_string = "[]"
        expected_output = []
        result = Rectangle.from_json_string(json_string)
        self.assertEqual(result, expected_output)

    def test_from_json_string_single_dict(self):
        json_string = '[{"height": 4, "width": 10, "id": 89}]'
        expected_output = [{"height": 4, "width": 10, "id": 89}]
        result = Rectangle.from_json_string(json_string)
        self.assertEqual(result, expected_output)

    def test_from_json_string_nested_dicts(self):
        json_string = '[{"rectangle": {"height": 4, "width": 10, "id": 89}}, {"square": {"size": 5, "id": 7}}]'
        expected_output = [{"rectangle": {"height": 4, "width": 10, "id": 89}}, {"square": {"size": 5, "id": 7}}]
        result = Rectangle.from_json_string(json_string)
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
