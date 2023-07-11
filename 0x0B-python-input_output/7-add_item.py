#!/usr/bin/env python
"""
This script takes command line arguments and adds them to a Python list.
The list is then saved to a JSON file.
"""
import sys
import json

def save_to_json_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_from_json_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)

if __name__ == "__main__":
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []
    items.extend(sys.argv[1:])
     save_to_json_file(items, "add_item.json")
