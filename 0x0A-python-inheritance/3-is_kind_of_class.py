#!/usr/bin/python3
"""
Module introduces a dunction for checking boolen expression.
"""


def is_kind_of_class(obj, a_class):
    """
    Function that returns trueof false.

    Args:
        obj: The object to check.

    Returns:
        True if obj is an instance of a_class; otherwise False.
    """

    return isinstance(obj, a_class)
