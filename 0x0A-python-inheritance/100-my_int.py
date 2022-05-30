#!/usr/bin/python3
"""
Write a class MyInt that inherits from int
MyInt is a rebel. MyInt has == and != operators inverted
"""


class MyInt(int):
    """class MyInt"""
    def __init__(self, value=0):
        self.value = value

    def __eq__(self, other):
        return self.value != other

    def __ne__(self, other):
        return self.value == other
