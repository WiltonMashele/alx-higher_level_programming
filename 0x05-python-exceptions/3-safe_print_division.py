#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        num_div = a / b
        print("Inside result: {}".format(num_div))
    except (TypeError, ZeroDivisionError):
        num_div = None
        print("Error occurred during division")
    return num_div
