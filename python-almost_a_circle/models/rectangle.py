#!/usr/bin/python3
"""
lsadgfshgjhdfhdgseasrdtfjyfjthrgaestr\
    dgfesasrgdhftrgserawestrdytfrte
"""
from models.base import Base


class Rectangle(Base):
    """xdfgchvjklljhgfhjkl"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """yuitueryetawtrtyueyryet"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """x getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return the area of rectangle"""
        return self.__height * self.__width

    def display(self):
        """display the rectangle"""
        rect_str = ""
        for _ in range(self.__height):
            rect_str += str("#") * self.__width + "\n"
        print(rect_str.rstrip("\n"))

    def __str__(self):
        """return rectangle representation"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y}"\
            f" - {self.width}/{self.height}"
