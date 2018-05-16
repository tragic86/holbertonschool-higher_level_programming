#!/usr/bin/python3
"""
checking same object
"""


def is_same_class(obj, a_class):
    """compare class and object"""

    if type(obj) is a_class:
        return True
    else:
        return False
