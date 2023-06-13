#!/usr/bin/python3
'''
This module introduces a function.
'''
import json


def save_to_json_file(my_obj, filename):
    """
    Function that writes an Object to a text, using Json representation.
    Args:
        my_obj
        filename: Name of the file.
    """

    with open(filename, 'w') as f:
        json.dump(my_obj, f)
