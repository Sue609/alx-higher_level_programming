#!/usr/bin/python3
"""
This module introduces a class called MyInt.
"""


class MyInt(int):
    """
    The class inherits from int. MyInt is a rebel.
    """

    def __eq__(self, other):
        """
        Overrides the equality (==) operator.
        """
        
        return (super().__ne__(other))

    def __ne__(self, other):
        """
        Overrides the inequality (!=) operator.
        """

        return (super().__eq__(other))
