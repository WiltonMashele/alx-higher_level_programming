#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    all_dir = dir(hidden_4)
    for item in all_dir:
        if not item.startswith("__"):
            print(item)
