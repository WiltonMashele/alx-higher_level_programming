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
    if isinstance(obj, dict):
        obj[att] = value
    else:
        raise TypeError("Unable to add new attribute.")
