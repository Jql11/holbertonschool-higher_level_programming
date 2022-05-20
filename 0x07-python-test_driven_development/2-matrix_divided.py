#!/usr/bin/python3
"""divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """
    returns a new matrix
    """

    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(msg)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        new_row = []
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        if not isinstance(row, list):
            raise TypeError(msg)
        for n in row:
            if not isinstance(n, (int, float)):
                raise TypeError(msg)
            new_row.append(round(n/div, 2))
        new_matrix.append(new_row)
    return new_matrix
