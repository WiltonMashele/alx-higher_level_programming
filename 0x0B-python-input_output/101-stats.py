#!/usr/bin/python3
"""
Reads input from the user and calculates metrics.

After every five inputs or if the user interrupts the program (CTRL + C),
it displays the following statistics:
    - Total sum of the inputs up to that point.
    - Count of unique inputs up to that point.
"""


def print_statistics(total_sum, count):
    """
    Prints accumulated metrics.

    Args:
        total_sum (int): The accumulated sum of inputs.
        count (int): The accumulated count of unique inputs.
    """
    print("Total sum: {}".format(total_sum))
    print("Count of inputs: {}".format(count))


if __name__ == "__main__":
    total_sum = 0
    count = 0
    unique_inputs = set()

    try:
        while True:
            user_input = input("Enter a number: ")

            total_sum += int(user_input)
            unique_inputs.add(user_input)
            count += 1

            if count == 5:
                print_statistics(total_sum, len(unique_inputs))
                count = 0

    except KeyboardInterrupt:
        print_statistics(total_sum, len(unique_inputs))
        raise

