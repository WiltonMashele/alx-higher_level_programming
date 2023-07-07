#!/usr/bin/python3
"""Defines a function for integer addition."""


def add_integer(a, b=98):
    """Return the integer addition of a and b.

    If a or b is a float, it is converted to an integer before the addition is performed.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    return int(a) + int(b)
