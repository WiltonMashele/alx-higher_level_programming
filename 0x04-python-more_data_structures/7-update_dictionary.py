#!/usr/bin/python3

def update_dictionary(my_dict, key, value):
    return dict(my_dict, **{key: value})
