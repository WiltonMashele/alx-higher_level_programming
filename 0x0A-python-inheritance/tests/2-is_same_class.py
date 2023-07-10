#!/usr/bin/python3
"""
This function determines if an object is an instance of a specified class.
Returns True if the object is an instance; otherwise, returns False.
"""


def is_same_class(obj, a_class):
    """
    Checks if the object is an instance of a specified class.

    Parameters:
    obj (any): The object to be checked.
    a_class (type): The class to compare the object's type with.

    Returns:
    bool: True if the object is an instance of the specified class; False otherwise.
    """
    return type(obj) is a_class
