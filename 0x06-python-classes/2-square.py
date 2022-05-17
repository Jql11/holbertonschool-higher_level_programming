#!/usr/bin/python3
"""
Module 2-square
Defines class Square with private attribute size and validates size
"""


class Square:
    """define a class"""
    def __init__(self, size=0):
        """private instance attribute
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
