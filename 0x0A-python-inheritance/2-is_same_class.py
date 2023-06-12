#!/usr/bin/python3
"""
This module introduces a function.
Function returns either true or false based on the instance of the object.
Author: Susan
"""


def is_same_class(obj, a_class):
    """
    Function that returns either True of False.

    Args:
        obj (any): The object to check.
        a_class (class): The class to compare against.

    Return:
        bool: True, False otherwise.
    """

    return type(obj) is a_class
