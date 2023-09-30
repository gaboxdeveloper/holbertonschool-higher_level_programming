#!/usr/bin/python3
"""Class called square"""


class Square:
    def __init__(self, size=0):
        self.size = size  # Use the property setter to set the size

    @property
    def size(self):
        return self.__size  # Getter for size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value  # Private instance attribute

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
