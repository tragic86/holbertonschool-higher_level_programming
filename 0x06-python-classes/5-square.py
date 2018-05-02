#!/usr/bin/python3


class Square:
    """empty square"""

    def __init__(self, size=0):
        """
        Args:

            param1 (size): size of square

        """
        self.__size = size

    def area(self):
        """get area"""
        return self.__size * self.__size

    @property
    def size(self):
        """setter for size"""

        return self.__size

    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints a # square depending on size."""
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end='')
            print()
        if self.__size == 0:
            print()
