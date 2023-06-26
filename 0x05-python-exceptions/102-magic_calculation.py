#!/usr/bin/python3

def magic_calculation(a, b):
    result = 0
    
    if a > b:
        result = (a * b) - a
    elif a < b:
        result = (a + b) - b
    else:
        result = a * b
        
    return result
