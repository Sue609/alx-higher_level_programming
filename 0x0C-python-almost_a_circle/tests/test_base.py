#!/usr/bin/python3

import unittest

from models.base import Base

class TestBaseClass(unittest.TestCase):
    def test_constructor_with_id(self):
        base = Base(id=5)
        self.assertEqual(base.id, 5)

    def test_constructor_without_id(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

    def test_attributes_custom(self):
        base = Base(id=10)
        base.name = "Susan"
        self.assertEqual(base.name, "Susan")

    def test_private_attributes(self):
        base = Base()
        with self.assertRaises(AttributeError):
            base.__nb_objects

    def test_if_subclass_inherits_id(self):
        class Subclass(Base):
            def __init__(self, id=None):
                super().__init__(id=id)

        subclass = Subclass()
        self.assertEqual(subclass.id, 3)

    def test_to_json_string_empty(self):
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_none(self):
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_to_json_single_dict(self):
        list_of_dicts = [{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]
        result = Base.to_json_string(list_of_dicts)
        self.assertEqual(result, '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]')

    def test_to_json_string_multiple_dicts(self):
        list_of_dicts = [
                {"x": 2, "width": 10, "id": 1, "height": 7, "y": 8},
                {"x": 5, "width": 6, "id": 2, "height": 3, "y": 4}
            ]
        result = Base.to_json_string(list_of_dicts)
        self.assertEqual(result, '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}, '
                                 '{"x": 5, "width": 6, "id": 2, "height": 3, "y": 4}]')

    def test_to_json_string_nested_dicts(self):
        nested_dicts = [
                {"x": 2, "nested": {"a": 1, "b": 2}},
                {"x": 5, "nested": {"c": 3, "d": 4}}
            ]
        result = Base.to_json_string(nested_dicts)
        self.assertEqual(result, '[{"x": 2, "nested": {"a": 1, "b": 2}}, '
                             '{"x": 5, "nested": {"c": 3, "d": 4}}]')

    
if __name__ == '__main__':
    unittest.main()
