#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """
    A function that prints an integer
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
