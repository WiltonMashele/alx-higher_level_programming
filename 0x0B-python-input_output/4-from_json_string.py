#!/usr/bin/python3
"""
This module defines a function that converts a JSON string into an object.
"""
import json


def from_json_string(json_str):
    """
    Converts a JSON string into an object.

    Args:
        json_str (str): The JSON string to be converted.

    Returns:
        object: The object representation of the JSON string.

    Raises:
        ValueError: If the JSON string is invalid.

    """
    return json.loads(json_str)
