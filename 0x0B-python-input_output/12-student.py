#!/usr/bin/python3
"""
function to json
"""


class Student:
    """create class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        i = {}
        if attrs is None:
            return self.__dict__

        for key, value in self.__dict__.items():
            if key in attrs:
                i[key] = value
        return i
