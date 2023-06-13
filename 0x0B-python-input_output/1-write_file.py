#!/usr/bin/python3
"""
This module introduces a function we are supposed to write a file.
"""


def write_file(filename="", text=""):
    """
    This function writes a string to a text file.
    """

    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(text)
            return len(text)
    except IOError:
        return 0

