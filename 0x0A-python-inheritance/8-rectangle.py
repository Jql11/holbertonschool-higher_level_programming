#!/usr/bin/python3
"""
Write a class Rectangle that inherits from BaseGeometry
Instantiation with width and height: def __init__(self, width, height)
width and height must be private. No getter or setter
width and height must be positive integers, validated by integer_validator
"""


class BaseGeometry:
    """class"""

    def area(self):
        """rasie exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value
        assume name always string
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ inherited class from BaseGeometry"""
    def __init__(self, width, height):
        """ instantiation with width and height"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
