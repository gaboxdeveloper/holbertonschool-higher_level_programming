#!/usr/bin/python3
"""lalala"""


class BaseGeometry:
    """not an empty class"""
    def area(self):
        """function"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function to validate an itenger"""
        self.name = name
        if type(value) is not int:
            raise TypeError(f"{self.name} must be an integer")
        if value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")
        if not value:
            raise TypeError(f"{self.name} is missing the value")
