#!/usr/bin/env python
"""
This script takes command line arguments and adds them to a Python list.
The list is then saved to a JSON file.
"""
import sys
import json

f __name__ == "__main__":
    try:
        with open("add_item.json", "r") as file:
            items = json.load(file)
    except FileNotFoundError:
        items = []
    items.extend(sys.argv[1:])
    with open("add_item.json", "w") as file:
        json.dump(items, file)
