#!/usr/bin/python3

def best_score(my_dict):
    if not my_dict:
        return None
    best_player = max(my_dict, key=my_dict.get)
    return best_player
