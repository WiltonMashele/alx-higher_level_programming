#!/usr/bin/python3
output = ""
for ch in range(97, 123):
    if ch not in [101, 113]:
        output += "{:c}".format(ch)
print(output, end='')
