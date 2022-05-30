#!/usr/bin/python3
"""
Public instance method:
def area(self):
that raises an Exception with the message area() is not implemented
"""


class BaseGeometry:
    """public instance method"""
    def area(self):
        """exception that area is not implemented"""
        raise Exception("area() is not implemented")
