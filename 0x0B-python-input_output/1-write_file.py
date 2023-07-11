#!/usr/bin/python3
"""Defines a function for appending text to a file."""


def append_write(filename="", text=""):
    """
    Writes a string to a UTF-8 text file, overwriting the previous contents.
    Args:
        filename (str): The name of the file to write to.
        text (str): The string to write to the file.
    Returns:
        int: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
