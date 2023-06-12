#!/usr/bin/python3
"""
Module introduces a dunction for checking boolen expression.
"""


def is_kind_of_class(obj, a_class):
    """
    Function that returns true if the object is an instance of or if the
    object is an instance of a class that inherited from, the specified class 
    or otherwise false.

    Args:
        obj: The object to check.

    Returns:
        True if obj is an instance of a_class; otherwise False.
    """

    return isinstance(obj, a_class)
