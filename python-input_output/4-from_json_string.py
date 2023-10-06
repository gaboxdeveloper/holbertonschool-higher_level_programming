#!/usr/bin/python3
"""Write a function that returns an object
(Python data structure) represented by a JSON
string"""
import json


def from_json_string(my_obj):
    """returning json an obj repr by json"""
    return json.dumps(my_obj)
