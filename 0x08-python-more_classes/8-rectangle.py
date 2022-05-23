#!/usr/bin/python3
"""
define a class Rectangle
private instance attribute width and height
public instance method area and perimeter
use print() and str() to print rectangle with #
repr() to return a string representation of the rectangle
print the message when instance of Rectangle is deleted
Public class attribute number_of_instances
public class attribute print_symbol

"""


class Rectangle():
    """class rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initialization"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
        x = "\n".join(str(self.print_symbol) * self.__width
                      for rows in range(self.__height))
        return x

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
