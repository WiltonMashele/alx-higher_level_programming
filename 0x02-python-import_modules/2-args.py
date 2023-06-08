#!/usr/bin/python3

import sys

if __name__ == "__main__":
    total = len(sys.argv)
    if total <= 1:
        print("0 arguments.")
    else:
        if total == 2:
            print(f"1 argument: {sys.argv[1]}")
        else:
            print(f"{total-1} arguments:")
            for i in range(1, total):
                print(f"{i}: {sys.argv[i]}")
