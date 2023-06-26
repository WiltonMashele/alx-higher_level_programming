#!/usr/bin/python3

import sys

def safe_function(fct, *args):
    """
    A function that executes a function safely
    """
    try:
        result = fct(*args)
        return result
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print("Exception: {}".format(exc_value), file=sys.stderr)
        return None
