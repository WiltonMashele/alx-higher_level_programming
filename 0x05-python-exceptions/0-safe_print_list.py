#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    cmpt = 0
    iterator = iter(my_list)
    
    while cmpt < x:
        try:
            print(next(iterator), end='')
            cmpt += 1
        except StopIteration:
            break
        except:
            break
    
    print('')
    return cmpt
