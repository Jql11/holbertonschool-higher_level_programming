#!/usr/bin/python3
"""
Class Base
private class attribute __nb_objects = 0
assume id is integer, no need to test type of it
"""
import json


class Base:
    """class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """if id is none, increment __nb_object and assign new value to id
        otherwise assign id with this argument value
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """return JSON string representation"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """write the JSON string representation of list_objs to a file"""
        objs = []
        if list_objs is not None:
            for ob in list_objs:
                if isinstance(ob, Base):
                    objs.append(cls.to_dictionary(ob))
        json_string = cls.to_json_string(objs)
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """return the list of the JSON string"""
        if json_string is None or len(json_string) == 0:
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """return an instance with all attributes already set"""
        if cls.__name__ == "Square":
            dummy = cls(1)
            print(dummy)
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """return a list of instances"""
        filename = cls.__name__ + ".json"
        lis = []
        try:
            with open(filename, "r") as f:
                instances = cls.from_json_string(f.read())
            for ele in instances:
                lis.append(cls.create(**ele))
        except Exception:
            pass
        return lis
