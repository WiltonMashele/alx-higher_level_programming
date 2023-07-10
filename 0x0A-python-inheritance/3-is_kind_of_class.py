#!/usr/bin/python3
"""
Check class and subclass
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of, or if the object is 
    an instance of a class that inherited from,
    the specified class. Return True if it is, otherwise False.
    """
    return isinstance(obj, a_class)
