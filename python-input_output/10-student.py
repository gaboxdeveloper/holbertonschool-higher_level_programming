#!/usr/bin/python3
"""
Write a class Student that defines a student by:

Public instance attributes:
first_name
last_name
age
"""


class Student:
    """class student
    maybe I need more lines"""
    def __init__(self, first_name, last_name, age):
        """instantiation function
        maybe I need more lines"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance."""
        if attrs is None:
            return self.__dict__
        return {attr: getattr(self, attr)
                for attr in attrs if hasattr(self, attr)}
