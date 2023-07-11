#!/usr/bin/python3
"""This script defines a function to generate Pascal's Triangle."""

def generate_pascals_triangle(n):
    """Generates Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        row = triangle[-1]
        next_row = [1]
        for i in range(len(row) - 1):
            next_row.append(row[i] + row[i + 1])
        next_row.append(1)
        triangle.append(next_row)
    return triangle
