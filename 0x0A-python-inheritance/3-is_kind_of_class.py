#!/usr/bin/python3
"""
checking same object
"""


def is_kind_of_class(obj, a_class):
    """compare class and object"""

    if not isinstance(obj, a_class):
        return False
    else:
        return True
