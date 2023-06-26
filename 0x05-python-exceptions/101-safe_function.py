#!/usr/bin/python3

import sys
import traceback

def safe_function(fct, *args):
    """
    A function that executes a function safely
    """
    try:
        result = fct(*args)
        return result
    except Exception:
        traceback.print_exc(file=sys.stderr)
        return None
