#!/usr/bin/python3
"""Write a function that returns the
JSON representation of an object (string):"""
import json


def to_json_string(my_obj):
    """returning json repr of an obj string"""
    return json.JSONEncoder().encode(my_obj)
