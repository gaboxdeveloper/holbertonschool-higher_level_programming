#!/usr/bin/python3
"""module of a rectangle!"""
Rectangle = __import__('9-rectangle').rectangle


class Square():
    """class Square"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """return the area of the rectangle"""
        return self.size ** 2
