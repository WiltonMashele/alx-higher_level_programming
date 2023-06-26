#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    list_count = 0
    try:
        for element in range(x):
            print("{:d}".format(my_list[element]), end="")
            list_count += 1
    except IndexError:
        pass
    print("")
    return list_count
