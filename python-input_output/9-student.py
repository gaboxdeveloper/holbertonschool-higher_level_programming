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

    def to_json(self):
        """to json public methodç
        maybe I need more lines"""
        if isinstance(self.first_name, (dict, str, int, bool)):
            return self.first_name
        elif isinstance(self.first_name, (list, tuple)):
            return [item.to_json() for item in self.first_name]
        elif hasattr(self.first_name, '__dict__'):
            serializable_dict = {}
            for key, value in self.first_name.__dict__.items():
                if hasattr(value, 'to_json'):
                    serialized_value = value.to_json()
                else:
                    None
                serializable_dict[key] = serialized_value
            return serializable_dict
        else:
            return None
