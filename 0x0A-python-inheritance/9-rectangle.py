#!/usr/bin/python3
"""
Instantiation with width and height: def __init__(self, width, height)
the area() method must be implemented
print() should print, and str() should return
the following rectangle description: [Rectangle] <width>/<height>
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

    def area(self):
        """implemented"""
        return self.__width * self.__height

    def __str__(self):
        return("[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                       self.__width, self.__height))
