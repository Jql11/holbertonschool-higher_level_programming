#!/usr/bin/python3
"""
Write a class MyList that inherits from list
"""


class MyList(list):
    """ class"""
    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
