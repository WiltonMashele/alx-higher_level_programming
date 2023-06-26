#!/usr/bin/python3

"""a function that divides 2 integers and prints the result."""

def safe_print_division(a, b):
    try:
        num_div = a / b
    except ZeroDivisionError:
        num_div = None
    except TypeError:
        num_div = None
    finally:
        print("Inside result: {}".format(num_div))
    return num_div
