#!/usr/bin/python3
"""
class Square that inherits from Rectangle
Instantiation with size: def __init__(self, size)
the area() method must be implemented
print() should print, and str() should return,
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class Square
    Instantiation with size
    area() method must be implemented
    """
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
