#!/usr/bin/python3
"""Defines a function for writing text to a file."""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 encoded text file.

    Args:
        filename (str): The name of the file to write. Default is an empty string.
        text (str): The text to write to the file. Default is an empty string.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
