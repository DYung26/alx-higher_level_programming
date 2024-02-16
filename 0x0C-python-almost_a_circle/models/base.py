#!/usr/bin/python3
"""
base module
"""
import json


class Base:
    """
    Attributes:
        id: (int)

    Args:
        __nb_objects: (int)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs:
            listObjs = [i.to_dictionary() for i in list_objs]
            with open("Rectangle.json", "w") as file:
                file.write(cls.to_json_string(listObjs))
