#!/usr/bin/python3
def fizzbuzz():
    output = ""
    for i in range(1, 101):
        if i % 15 == 0:
            output += "FizzBuzz "
        elif i % 3 == 0:
            output += "Fizz "
        elif i % 5 == 0:
            output += "Buzz "
        else:
            output += str(i) + " "
    print(output)
