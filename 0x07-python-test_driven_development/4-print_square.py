#!/usr/bin/python3
"""
Function to print square


"""


def print_square(size):
    """ if size isnt int"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    """ if size isnt float and less that zero"""
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")
    """ Print hash"""
    for i in range(size):
        for j in range(size):
            print('#', end=" ")
        print()
