#!/usr/bin/python3
"""write a function that divides all elements of a matrix
matrix must be a list of lists of integers or floats
each row of the matrix myst be of the same size
div must be a number(integer or float) and can't be 0
returns a new matrix, rounded to 2 decimal places"""


def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix
    returns new matrix
    """

    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(msg)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(msg)
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for n in row:
            if not isinstance(n, (int, float)):
                raise TypeError(msg)
            new_row.append(round(n/div, 2))
        new_matrix.append(new_row)
    return new_matrix
