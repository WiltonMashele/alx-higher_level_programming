#!/usr/bin/python3
from add_0 import add

def add_numbers(a, b):
    return add(a, b)

if __name__ == "__main__":
    a = 1
    b = 2
    result = add_numbers(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, result))
