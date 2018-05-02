#!/usr/bin/python3


class Square:
    """empty square"""

    def __init__(self, size=0):
        """
        Args:
            param1 (size): size of square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """get area"""
        return self.__size * self.__size
