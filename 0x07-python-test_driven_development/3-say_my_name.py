#!/usr/bin/python3
"""Defines a function to print a name."""


def print_name(first_name, last_name=""):
    """Print a name.

    Args:
        first_name (str): The first name to print.
        last_name (str): The last name to print. Defaults to an empty string.
    Raises:
        TypeError: If either first_name or last_name are not strings.
    """
    if type(first_name) != str:
        raise TypeError("The first name must be a string")
    if type(last_name) != str:
        raise TypeError("The last name must be a string")
    print("Name: {} {}".format(first_name, last_name))
