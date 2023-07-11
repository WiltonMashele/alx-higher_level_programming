#!/usr/bin/python3
"""Module to check class and subclass""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of the specified class or 
    any of its subclasses; otherwise, it returns False.
    """
    return isinstance(obj, a_class)
