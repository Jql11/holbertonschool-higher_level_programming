#!/usr/bin/python3
"""
This is the 0-add_integer module

The example module supplies one function, add_integer(). For example,

>>> add_integer(1, 2)
3
"""


def add_integer(a, b=98):
    """returns an integer: the addition of a and b"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
