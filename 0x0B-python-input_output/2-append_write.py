#!/usr/bin/python3
"""
This module introduces a function for python input-output.
"""


def append_write(filename="", text=""):
    """
    This function appends a string at the end of a text file.
    Returns:
        The number of characters added to the file.
    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
