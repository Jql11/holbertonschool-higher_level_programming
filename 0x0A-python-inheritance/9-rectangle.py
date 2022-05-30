#!/usr/bin/python3
"""
Instantiation with width and height: def __init__(self, width, height)
the area() method must be implemented
print() should print, and str() should return
the following rectangle description: [Rectangle] <width>/<height>
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
