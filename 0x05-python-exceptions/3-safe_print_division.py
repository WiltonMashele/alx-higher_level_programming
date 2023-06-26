#!/usr/bin/python3

"""a function that divides 2 integers and prints the result."""

def safe_print_division(a, b):
    num_div = None
    try:
        num_div = a / b
    except (TypeError, ZeroDivisionError):
        pass
    finally:
        print("Inside result: {}".format(num_div))
    return num_div
