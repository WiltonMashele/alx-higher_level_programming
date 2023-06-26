#!/usr/bin/python3
def safe_print_integer(value):
    try:
        value = int(value)
    except TypeError:
        return False
    except ValueError:
        return False
    else:
        print("{:d}".format(value))
        return True
