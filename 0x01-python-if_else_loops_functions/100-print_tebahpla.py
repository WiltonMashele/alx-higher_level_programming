#!/usr/bin/python3
for i in range(25, -1, -1):
    offset = ord('A') - ord('a') if i % 2 == 0 else 0
    print('{}'.format(chr(i + ord('a') + offset)), end="")
