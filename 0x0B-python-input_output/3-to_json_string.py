#!/usr/bin/python3
import json
"""
This module introduces a function.
"""


def to_json_string(my_obj):
    """
    This function returns the JSON representation of an object.
    """

    try:
        return json.dumps(my_obj)
    except TypeError as e:
        raise TypeError(f"{my_obj} is not JSON serializable")
