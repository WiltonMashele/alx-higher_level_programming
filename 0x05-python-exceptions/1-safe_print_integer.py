#!/usr/bin/python3

def safe_print_integer(value):
    try:
        value_str = "{:d}".format(value)
        print(value_str)
        return True
    except (KeyError, IndexError):
        return False
    except ValueError:
        return False
