#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    element = 0

    while True:
        try:
            print("{:d}".format(my_list[element]), end="")
            count += 1
            element += 1
        except (ValueError, TypeError, IndexError):
            element += 1
        if element >= x:
            break

    print("")
    return count
