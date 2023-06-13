#!/usr/bin/python3
"""
This module introduces a function.
"""


def read_file(filename=""):
    """
    This function reads a text file and prints it to stdout.
    Args:
        filename: Name of th file.
    """

    with open(filename, mode="r", encoding="utf-8") as file:
        for line in file:
            print(line, end='')
