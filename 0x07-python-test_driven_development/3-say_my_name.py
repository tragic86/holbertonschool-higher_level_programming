#!/usr/bin/python3
"""

Function to print a name

"""


def say_my_name(first_name, last_name=""):

    """if name is not string"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

        """if name is not string"""
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    """print name"""
    print("Hi my name is {} {}".format(first_name, last_name))
