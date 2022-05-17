#!/usr/bin/python3
"""define a class Square"""


class Square:
    """define a class"""
    def __init__(self, size=0):
        """initialise square"""
        self.__size = size

    @property
    def size(self):
        """getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """public instance method
        return current square area
        """
        return int(self.__size) * int(self.__size)
