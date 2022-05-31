#!/usr/bin/python3
"""
Write a class Student that defines a student by
first name
last name
age
"""


class Student:
    """class Student"""
    def __init__(self, first_name, last_name, age):
        """instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance
        return attrs given to us
        if no attrs, return all
        """
        if attrs is None:
            return self.__dict__
        else:
            dic = {}
            for ele in attrs:
                if ele in self.__dict__.keys():
                    dic[ele] = self.__dict__[ele]
            return dic
