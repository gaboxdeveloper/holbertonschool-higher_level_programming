#!/usr/bin/python3
"""Class called square"""


class Square:
    """This class is made
    to create a square"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size