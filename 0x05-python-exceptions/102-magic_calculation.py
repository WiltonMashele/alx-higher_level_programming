#!/usr/bin/python3

def magic_calculation(a, b):
    result = 0

    if a < 1:
        result = b + a
    else:
        result = (a ** b) / (1 + 2)

    return result
