#!/usr/bin/python3
"""
This module introduces a function.
Function returns either true or false based on the instance of the object
"""


def is_same_class(obj, a_class):
    """
    Function that returns True if the object is exactly an instance of the
    specified class or otherwise False.

    Args:
        obj (any): The object to check.
        a_class (class): The class to compare against.

    Return:
        bool: True if the object is an instance of the specified class, False otherwise.
    """

    return type(obj) is a_class
