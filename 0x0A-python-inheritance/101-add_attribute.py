#!/usr/bin/python3
"""
In this module we introduce a function that adds a new attribute to an object
if possible.
"""


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if possible.

    Args:
        obj: The object to add the attribute to.
        attr: The name of the attribute.
        value: The value to assign to the attribute.

    Raises:
        TypeError: If the object cannot have a new attribute.
    """

    if hasattr(obj, '__dict__'):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
