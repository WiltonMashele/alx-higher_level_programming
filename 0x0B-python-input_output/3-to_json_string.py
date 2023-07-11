#!/usr/bin/python3
"""Defines a function to convert a Python object to a JSON string."""


import json


def to_json_string(my_obj):
    """
    Return the JSON representation of a Python object.

    Args:
        my_obj (object): The Python object to be converted to JSON.
    Returns:
        str: The JSON string representing the Python object.
    """
    return json.dumps(my_obj)

