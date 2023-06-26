#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    list_count = 0
    element = 0
    while True:
        try:
            print("{:d}".format(my_list[element]), end="")
            list_count += 1
            element += 1
        except IndexError:
            break
        except:
            element += 1
    print("")
    return list_count
