#!/usr/bin/python3
"""
This module intoduces a the first class.
"""
import json


class Base:
    """
    This is the first class in this file which is the base
    of all other classes in this project.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        This is a class constructor to set attributes.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Static method that returns JSON string representation.
        Args:
            list_dictionaries: A list of dicts
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)


if __name__ == '__main__':
    unittest.main()
