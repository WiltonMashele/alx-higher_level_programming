#!/usr/bin/python3
"""This program reads a text file and prints its contents to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and
    prints its contents to the standard output. Does not return any value.
    """
    with open(filename, 'r', encoding="utf-8") as f:
    read_data = ''.join(f.readlines())
    print(read_data, end='')
