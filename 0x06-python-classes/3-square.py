#!/usr/bin/python3
"""define a class Square"""


class Square:
    def __init__(self, size=0):
        """private instance attribute
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """public instance method
        Return area
        """
        return int(self.__size) * int(self.__size)
