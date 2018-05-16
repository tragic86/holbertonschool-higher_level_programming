#!/usr/bin/python3
"""inherits class"""


def inherits_from(obj, a_class):
    """compare class and object"""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
