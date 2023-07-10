#!/usr/bin/python3
"""
This function returns True if the object is an instance of the specified class;
otherwise, it returns False.
"""


def is_same_class(obj, a_class):
    """Checks if the object is an instance of a specified class"""
    return type(obj) is a_class
