#!/usr/bin/python3
"""
adds a new attribute to an object if it’s possible
"""

def newAttr(obj, attr, value):
    if hasattr(obj, '__dict__'):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")

