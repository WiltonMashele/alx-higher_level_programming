#!/usr/bin/python3
def safe_print_division(a, b):
    """Returns the division of a by b."""
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    else:
        print("Inside result: {}".format(div))
    finally:
        if 'div' not in locals():
            print("Inside result: {}".format(div))
    return div
