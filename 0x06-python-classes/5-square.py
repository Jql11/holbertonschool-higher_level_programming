#!/usr/bin/python3
"""define a class Square"""


class Square:
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
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

    def my_print(self):
        """public instance method
        prints in stdout the square with the character #
        """
        if self.__size == 0:
            print("\n")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
