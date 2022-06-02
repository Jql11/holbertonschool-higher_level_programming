#!/usr/bin/python3
"""
Class Base
private class attribute __nb_objects = 0
assume id is integer, no need to test type of it
"""


class Base:
    """class"""
    __nb_objects = 0
    def __init__(self, id=None):
        """if id is none, increment __nb_object and assign new value to id
        otherwise assign id with this argument value
        """
        if id == None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
