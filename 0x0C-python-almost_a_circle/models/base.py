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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Method that writes json string rep to a file.
        """

        file_name = cls.__name__ + ".json"
        objects = []
        if list_objs is not None:
            objects = [obj.to_dictionary() for obj in list_objs]
        with open(file_name, "w") as file:
            file.write(cls.to_json_string(objects))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of JSON string representation.
        """

        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes alredy set.
        """

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = None

        if dummy is not None:
            dummy.update(**dictionary)
        return dummy


if __name__ == '__main__':
    unittest.main()
