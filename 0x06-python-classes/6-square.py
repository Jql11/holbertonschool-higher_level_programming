#!/usr/bin/python3
"""define a class Square"""


class Square:
    """define a class"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """getter 1"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter 1"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """getter 2"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter 2"""
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0] is not int or type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
            print("")
        else:
            for i in range(self.__position[1]):
                if self.position[1] > 0:
                    print("")
            for j in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
