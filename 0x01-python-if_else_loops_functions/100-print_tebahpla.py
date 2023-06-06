#!/usr/bin/python3
output = ''
for char in range(122, 96, -1):
    output += "{:c}".format(char if (char % 2 == 0) else char - 32)
print(output)
