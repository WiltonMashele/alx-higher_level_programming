#!/usr/bin/python3

def print_sorted_dictionary(my_dict):
    sorted_items = sorted(my_dict.items())
    for key, value in sorted_items:
        print('{}: {}'.format(key, value))
