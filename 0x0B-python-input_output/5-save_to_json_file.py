#!/usr/bin/python3
"""
Module that contains a function to deserialize a JSON representation into an object
"""
import json


def from_json_string(json_string):
    """
    Deserialize a JSON representation into an object
    Args:
        json_string (str): JSON representation

    Raises:
        ValueError: If the JSON string is invalid or cannot be decoded

    Returns:
        object: Deserialized object

    """
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        raise ValueError("Invalid JSON string: {}".format(str(e)))
