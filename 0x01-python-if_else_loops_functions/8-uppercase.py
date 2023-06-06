#!/usr/bin/python3
def uppercase(str):
    tmp = list(str)
    for i in range(len(tmp)):
        if 97 <= ord(tmp[i]) <= 122:
            tmp[i] = chr(ord(tmp[i]) - 32)
    print("{}\n".format("".join(tmp)), end='')
