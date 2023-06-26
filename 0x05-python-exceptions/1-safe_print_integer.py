#!/usr/bin/python3
def safe_print_integer(value):
    try:
        int_value = int(value)
    except:
        return False
    else:
        print("{:d}".format(int_value))
        return True
