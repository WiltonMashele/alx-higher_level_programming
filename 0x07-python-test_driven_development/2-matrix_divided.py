#!/usr/bin/python3
"""Defines a function for dividing a matrix."""

def matrix_divided(matrix, divisor):
    """Divides all elements of a matrix by a divisor.

    Args:
        matrix (list): A list of lists containing integers or floats.
        divisor (int/float): The number by which to divide the matrix.
    Raises:
        TypeError: If the matrix is not a valid matrix.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If the divisor is not a number.
        ZeroDivisionError: If the divisor is 0.
    Returns:
        A new matrix representing the result of the division.
    """

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(element, int) or isinstance(element, float))
                    for row in matrix for element in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(divisor, (int, float)):
        raise TypeError("divisor must be a number")

    return [list(map(lambda x: round(x / divisor, 2), row)) for row in matrix]
