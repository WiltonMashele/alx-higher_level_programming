#!/usr/bin/python3

def magic_calculation(a, b):
    result = 0
    
    if a == 0:
        result = b
    elif b == 0:
        result = a
    elif a > b:
        result = a - b
    else:
        result = a + b
        
    return result
