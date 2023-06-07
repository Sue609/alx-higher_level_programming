#!/usr/bin/python3

"""
This module provides a function for adding two integers.
"""

def add_integer(a, b=98):
    """
    Adds two integers and returns the result.

    Args:
        a (int or float): The first integer or float.
        b (int or float, optional): The second integer or float. Defaults to 98.

    Returns:
        int: The sum of the two integers.

    Raises:
        TypeError: If `a` or `b` is not an integer or float.

    Examples:
        >>> add_integer(5, 10)
        15
        >>> add_integer(2.5, 7)
        9
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
