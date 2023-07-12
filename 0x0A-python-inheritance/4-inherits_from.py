#!/usr/bin/python3
"""Defines a function to check inheritance relationship."""


def inherits_from(obj, a_class):
    """Checks if an object is an instance inherited from a specific class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare the type of obj with.

    Returns:
        bool: True if obj is an inherited instance of a_class, False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
