#!/usr/bin/python3

def magic_calculation(a, b):
    try:
        if a < 1 or b < 1:
            raise ValueError("Invalid input")
        result = a ** b / 1 + a ** b / 2
    except ValueError:
        result = b + a
    return result
