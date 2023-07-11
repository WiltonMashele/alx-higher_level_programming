#!/usr/bin/python3
"""Module containing a function to convert an object to its JSON representation"""
import json


def to_json_string(obj):
    """Converts an object to its JSON representation.

    Args:
        obj: The object to be converted.

    Returns:
        str: The JSON representation of the object.

    Raises:
        TypeError: If the object is not JSON serializable.

    """
    try:
        return json.dumps(obj)
    except TypeError as e:
        raise TypeError("Object is not JSON serializable: {}".format(e))
