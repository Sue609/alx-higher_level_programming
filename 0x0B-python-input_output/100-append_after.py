#!/usr/bin/python3
"""
Module that introduces a function.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Appends a line of text in a file.

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The string to search for in each line.
        new_string (str): The string to insert.

    Returns:
        None

    """
    with open(filename, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
        file.truncate()
