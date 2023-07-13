#!/usr/bin/python3
"""Defines a function that enhances objects with attributes."""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if feasible.

    Args:
        obj (any): The object to which an attribute will be added.
        att (str): The name of the attribute to be added to obj.
        value (any): The value of att.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, att, value)

