#!/usr/bin/python3
"""Class called square"""


class Square:
    """This class is made
    to create a square"""
    def __init__(self, size=0):
        try:
            self.__size = int(size)
        except Exception:
            if size < 0:
                raise ValueError("size must be >= 0")
            if size is not isinstance(size, int):
                raise TypeError("size must be an integer")
