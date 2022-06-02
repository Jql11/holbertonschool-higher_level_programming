#!/usr/bin/python3
"""class Rectangle inherits from Base"""


from models.base import Base


class Rectangle(Base):
    """inherited class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """private instance attribute"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter width"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter width"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """getter width"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter width"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """getter width"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter width"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """returns the area value"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout with # by taking care of x and y"""
        for i in range(self.__y):
            print("")
        for ele in range(self.__height):
            print(" " * self.__x + '#' * self.__width)

    def __str__(self):
        """return string message"""
        return f"[{self.__class__.__name__}] "\
               f"({self.id}) {self.__x}/{self.__y} - "\
               f"{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """order:id, width, height, x, y"""
        if args:
            for count, ele in enumerate(args):
                if count == 0:
                    self.id = ele
                if count == 1:
                    self.__width = ele
                if count == 2:
                    self.__height = ele
                if count == 3:
                    self.__x = ele
                if count == 0:
                    self.__y = ele
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'width':
                    self.__width = value
                if key == 'height':
                    self.__height = value
                if key == 'x':
                    self.__x = value
                if key == 'y':
                    self.__y = value
