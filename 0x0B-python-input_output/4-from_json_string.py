#!/usr/bin/python3
import json
"""
This module introduces a function.
"""


def from_json_string(my_str):
    """
    This function returns an object represented by a JSON string.
    """

    try:
        return json.loads(my_str)
    except json.JSONDecodeError as e:
        print("[{}] {}".format(e.__class__.__name__, e))
        return None
