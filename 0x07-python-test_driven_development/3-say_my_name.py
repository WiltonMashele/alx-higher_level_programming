#!/usr/bin/python3
"""Defines a function to print a name."""


def say_my_name(first_name, last_name=""):
    """Print a name.

    Args:
        first_name (str): The first name to print.
        last_name (str): The last name to print. Defaults to an empty string.
    Raises:
        TypeError: If either first_name or last_name are not strings.
    """
    try:
        full_name = " ".join(filter(None, [first_name, last_name]))
        print("My name is", full_name)
    except TypeError as e:
        raise TypeError("Both first_name and last_name must be strings") from e
