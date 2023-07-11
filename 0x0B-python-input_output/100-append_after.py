#!/usr/bin/env python3
""" Module for appending a line when a specific string is found """


def append_line(filename="", search_string="", new_string=""):
    """ Function to append a new line if a string is found

    Args:
        filename (str): Name of the file
        search_string (str): String to search for
        new_string (str): String to append

    """

    lines = []
    with open(filename, 'r', encoding="utf-8") as file:
        for line in file:
            lines.append(line.rstrip('\n'))
            if search_string in line:
                lines.append(new_string)

    with open(filename, 'w', encoding="utf-8") as file:
        file.write('\n'.join(lines))
