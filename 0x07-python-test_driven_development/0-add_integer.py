#!/usr/bin/python3
"""

This module add two integers

"""


def add_integer(a, b=98):
    """
    If a is float
    """
    if type(a) is float:
        a = int(a)

    """If b is float"""
    if type(b) is float:
        b = int(b)

    """If a is not an intger"""
    if type(a) is not int:

        """Error message"""
        raise TypeError("a must be an integer")

    """If b is not an intger"""
    if type(b) is not int:

        """Error message"""
        raise TypeError("b must be an integer")

    """return intgers"""
    return(a + b)
