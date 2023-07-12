#!/usr/bin/python3
"""
This script reads from standard input and computes metrics.

After every ten lines or upon receiving a keyboard interruption (CTRL + C),
it prints the following statistics:
- Total file size up to that point.
- Count of read status codes up to that point.
"""


def print_stats(size: int, status_codes: dict):
    """
    Print accumulated metrics.

    Args:
        size (int): The accumulated file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("Accumulated file size:", size)
    for code, count in sorted(status_codes.items()):
        print(f"{code}: {count}")


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, status_codes)
                count = 1
            else:
                count += 1

            line_parts = line.split()

            try:
                code = line_parts[-2]
                if code in valid_codes:
                    size += int(line_parts[-1])
                    status_codes[code] = status_codes.get(code, 0) + 1
            except (IndexError, ValueError):
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise

