#!/usr/bin/python3
"""
This module introduces function called inherit_from.
"""


def inherits_from(obj, a_class):
    """
    returns True if the object is an instance of a class
    otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True or False
    """

    return (issubclass(type(obj), a_class) and type(obj) != a_class)
