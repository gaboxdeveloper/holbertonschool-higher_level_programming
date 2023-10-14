#!/usr/bin/python3
"""
lsadgfshgjhdfhdgseasrdtfjyfjthrgaestr\
    dgfesasrgdhftrgserawestrdytfrte
"""
import json


class Base:
    """clase de base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Convert a JSON string to a list of dictionaries"""
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of instances to a JSON file"""
        if list_objs is None:
            list_objs = []

        filename = f"{cls.__name__}.json"
        with open(filename, 'w') as file:
            json_str = cls.to_json_string([obj.to_dictionary()
                                           for obj in list_objs])
            file.write(json_str)
