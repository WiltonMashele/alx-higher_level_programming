#!/usr/bin/python3
"""Defines a function for appending text to a file."""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a UTF8 text file.
    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        int: The number of characters appended.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        num_of_chars = f.write(text)
    return num_of_chars
