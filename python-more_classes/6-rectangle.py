#!/usr/bin/python3
"""Module where we will
make a class to create a rectangle"""


class Rectangle:
    """A rectangle where we define
    the width and the height.
    Those are private attributes, but we can modify them
    with the setter"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return (self.__width + self.__height) * 2

    def __str__(self):
        if self.__width == 0:
            return ""
        elif self.__height == 0:
            return ""
        else:
            rect_str = ""
            for _ in range(self.__height):
                rect_str += "#" * self.__width + "\n"
            return rect_str.rstrip("\n")

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
