#!/usr/bin/python3
"""
This module provides a function that converts an object into a dictionary,
suitable for JSON serialization, using a simple data structure.
"""


def class_to_json(obj):
    """
    Converts an object into a dictionary representation.

    Args:
        obj: The object to be converted.

    Returns:
        A dictionary representation of the object.
    """
    return vars(obj) if hasattr(obj, "__dict__") else {}
