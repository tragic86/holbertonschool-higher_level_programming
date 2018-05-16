#!/usr/bin/python3
"""
A Mylist
"""


class MyList(list):

    """Define class"""
    def print_sorted(self):
        """make print class
        """
        print(sorted(self))
