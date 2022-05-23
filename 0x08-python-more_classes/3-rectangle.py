#!/usr/bin/python3
"""
define a class Rectangle
private instance attribute width and height
public instance method area and perimeter
use print() and str() to print rectangle with #
"""


class Rectangle:
    """class rectangle"""
    def __init__(self, width=0, height=0):
        """initialization"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """public instance method area
        return the rectangle area
        """
        return int(self.__height) * int(self.__width)

    def perimeter(self):
        """public instance method
        return the rectangle perimeter
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (int(self.__height) + int(self.__width)) * 2

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        x = "\n".join(["#" * self.__width for rows in range(self.__height)])
        return x
