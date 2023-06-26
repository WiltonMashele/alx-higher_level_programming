#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    A function that divides element
    by element 2 lists
    """
    temp_list = []
    i = 0
    while i < list_length:
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            temp_list.append(result)
            i += 1
    
    return temp_list
