#!/usr/bin/python3
"""Defines a function for text indentation."""


def text_indentation(text):
    """Prints the text with indentation.

    Adds two new lines after each '.', '?', and ':' in the text.
    
    Args:
        text (str): The text to be printed.
        
    Raises:
        TypeError: If the input text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    index = 0
    while index < len(text) and text[index] == ' ':
        index += 1

    while index < len(text):
        print(text[index], end="")
        if text[index] == "\n" or text[index] in ".?:":
            if text[index] in ".?:":
                print("\n")
            index += 1
            while index < len(text) and text[index] == ' ':
                index += 1
            continue
        index += 1
