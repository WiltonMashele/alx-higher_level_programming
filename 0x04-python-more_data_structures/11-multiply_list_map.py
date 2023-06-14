#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    multiply_list = lambda my_list, number: list(map(lambda x: x * number, my_list))
    return multiply_list(my_list, number)
