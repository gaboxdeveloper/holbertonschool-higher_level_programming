#!/usr/bin/python3
"""
Write a function that creates an Object
from a “JSON file”:
"""
import json


def load_from_json_file(filename):
    """function that creates an Object
    from a “JSON file"""
    with open(filename, "r") as f:
        respuesta = json.load(f)
        return respuesta
