#!/usr/bin/python3
"""Base function"""
import json


class Base:
    """Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """json method"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file"""
        mt_list = []
        filename = cls.__name__ + '.json'
        if list_objs is None:
            mt_list = None
        else:
            for i in range(len(list_objs)):
                mt_list.append(cls.to_dictionary(list_objs[i]))
        with open(filename, 'w') as d:
                d.write(cls.to_json_string(mt_list))

    @staticmethod
    def from_json_string(json_string):
        """Return string"""
        m_list = []
        if json_string is None or len(json_string) == len(m_list):
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """make dummy class"""
        if cls.__name__ == 'Rectangle':
            dumb_class = cls(1, 2)
            dumb_class.update(**dictionary)
        else:
            cls.__name__ == 'Square'
            dumb_class = cls(1)
            dumb_class.update(**dictionary)
        return dumb_class

    @classmethod
    def load_from_file(cls):
        """load file"""
        mt_list = []

        filename = cls.__name__ + 'json'
        try:
            with open(filename, 'r', encoding='utf-8') as d:
                mt_list = cls.from_json_string(d.read())
            for i, j in enumerate(mt_list):
                mt_list[i] = cls.create(**mt_list[i])
        except:
            pass

        return mt_list
