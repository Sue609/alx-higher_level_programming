#!/usr/bin/python3
"""
This module introduces a class called MyInt.
"""


class MyInt(int):
    """
    The class inherits from int. MyInt is a rebel.

    MyInt has == and != operators inverted.
    """

    def __eq__(self, other):
        """
        Overrides the equality (==) operator.

        Args:
            others: The value to compare with.

        Returns:
            The inverted result of the equality check.
        """
        
        return (super().__ne__(other))

    def __ne__(self, other):
        """
        Overrides the inequality (!=) operator.

        Args:
            other: The value to compare with.

        Returns:
            The inverted result of the inequality check.
        """

        return (super().__eq__(other))