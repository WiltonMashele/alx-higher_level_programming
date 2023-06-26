#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    cmpt = 0
    index = 0

    while True:
        try:
            if index >= x:
                break
            print(my_list[index], end='')
            cmpt += 1
            index += 1
        except IndexError:
            break
        except:
            break

    print('')
    return cmpt
