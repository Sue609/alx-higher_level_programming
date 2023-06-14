#!/usr/bin/python3
"""
This file introduces a module class.
"""


class Student:
    """
    A class that defines a student by public instance attributes.
    """

    def __init__(self, first_name, last_name, age):
        """
        instantiation of the public attributes.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of student.
        """

        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
