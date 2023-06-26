#!/usr/bin/python3

"""a function that divides 2 integers and prints the result."""

def safe_print_division(a, b):
    try:
        num_div = a / b
    except (TypeError, ZeroDivisionError):
        num_div = None
    print("Inside result: {}".format(num_div))
    return num_div
