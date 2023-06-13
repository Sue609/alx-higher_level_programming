#!/usr/bin/python3
"""
This module introduces a function.
"""


def class_to_json(obj):
    """
    Convert an object to a dictionary representation with simple data structures for JSON serialization.
    """
    if isinstance(obj, str) or isinstance(obj, int) or isinstance(obj, bool):
        return obj
    elif isinstance(obj, list):
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: class_to_json(value) for key, value in obj.items()}
    elif hasattr(obj, "__dict__"):
        return class_to_json(obj.__dict__)
    elif hasattr(obj, "__slots__"):
        return class_to_json({slot: getattr(obj, slot) for slot in obj.__slots__})
    else:
        return str(obj)
