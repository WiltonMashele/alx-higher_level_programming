#!/usr/bin/python3
"""
This program reads a text file and prints its contents to stdout.
"""


def read_file(filename=""):
    """Reads a text file (assuming UTF-8 encoding) and prints its contents to the standard output.
    Does not return any value.
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            contents = f.read()
            print(contents, end="")
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("Error reading the file.")
