#!/usr/bin/python3
"""
This module introduces a function and imports a json lib.
"""
import json


def load_from_json_file(filename):
    """
    Function that creates an Object from "JSON  file"
    Args:
        filename: Name of the file.
    """

    with open(filename) as f:
        return json.load(f)
