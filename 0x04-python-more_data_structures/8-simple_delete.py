#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    new_dict = dict(my_dict)
    if key in new_dict:
        del new_dict[key]
    return new_dict
