#!/usr/bin/python3
"""Module that contains a function for appending text to a file."""


def append_write(filename="", text=""):
    """Append text to a file.

    Args:
        filename (str): Name of the file.
        text (str): Text to be written.

    Raises:
        Exception: If the file cannot be opened.
    """
    try:
        with open(filename, 'a') as file:
            file.write(text)
    except OSError:
        raise Exception("Unable to open or write to the file.")
