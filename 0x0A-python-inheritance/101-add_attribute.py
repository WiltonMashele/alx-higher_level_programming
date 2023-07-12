#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible.

    Args:
        obj (any): The object to which the attribute should be added.
        att (str): The name of the attribute to be added to `obj`.
        value (any): The value of the attribute `att`.
    Raises:
        TypeError: If the attribute cannot be added to `obj`.
    """
    if not hasattr(obj, att):
        obj.__setattr__(att, value)
    else:
        raise TypeError("Can't add new attribute")
