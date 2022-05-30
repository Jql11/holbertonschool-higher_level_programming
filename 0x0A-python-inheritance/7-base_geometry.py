#!/usr/bin/python3
"""
Public instance method: def area(self)
Public instance method: def integer_validator(self, name, value)
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
