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


if __name__ == '__main__':
    unittest.main()
