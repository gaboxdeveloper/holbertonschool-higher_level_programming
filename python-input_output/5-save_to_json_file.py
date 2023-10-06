#!/usr/bin/python3
"""
Write a function that writes an Object to a
text file, using a JSON representation:
"""
import json


def save_to_json_file(my_obj, filename):
    """funcion writes an object to a
    txt file using json"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
