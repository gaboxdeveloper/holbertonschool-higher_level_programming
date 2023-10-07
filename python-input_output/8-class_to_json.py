#!/usr/bin/python3
"""
Write a function that returns the dictionary description
with simple data structure (list, dictionary, string,
integer and boolean) for JSON serialization of an object:
"""


def class_to_json(obj):
    """function that returns the dictionary description"""
    if isinstance(obj, (dict, str, int, bool)):
        return obj
    if isinstance(obj, (list, tuple)):
        return [class_to_json(item) for item in obj]
    if hasattr(obj, '__dict__'):
        serializable_dict = {}
        for key, value in obj.__dict__.items():
            serializable_dict[key] = class_to_json(value)
        return serializable_dict
    return None
