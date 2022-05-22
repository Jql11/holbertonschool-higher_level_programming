#!/usr/bin/python3
"""This is the print_square module
The exampe module supplies one function, print_square(). For example,
>>> print_square(2)
##
##
"""


def print_square(size):
    """ prints a square with the character #
    size is the size length os the square
    size must be an integer
    size cannot be less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print("", end="")
    for row in range(size):
        print('#' * size)
