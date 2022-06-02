#!/usr/bin/python3
"""Square inherits from Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialization
        height = width"""
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[{self.__class__.__name__}]"\
                f"(<{self.id}>) <{self.x}>/<{self.y}> - <{self.size}>"

    @property
    def size(self):
        """getter size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assign attribute"""
        if args:
            for count, ele in enumerate(args):
                if count == 0:
                    self.id = ele
                if count == 1:
                    self.size = ele
                if count == 2:
                    self.x = ele
                if count == 3:
                    self.y = ele
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'size':
                    self.size = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value
