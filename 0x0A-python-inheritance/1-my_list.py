#!/usr/bin/python3
"""
This is the module docuumentation for my function.
The module intruduces a class which inherits from the list.
Author: Susan
"""

class MyList(list):
    """
    prints the list in sorted(ascending) order.

    Args:
        list(int): The list to be sorted.
    Returns:
        Nothing.
    """

    def print_sorted(self):
        print(sorted(self))
