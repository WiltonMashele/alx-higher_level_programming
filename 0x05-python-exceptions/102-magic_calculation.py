#!/usr/bin/python3

def magic_calculation(a, b):
    result = 0
    i = 1

    while i < 3:
        if i > a:
            result = b + a
            break
        else:
            result += a ** b / i
        i += 1

    return result
