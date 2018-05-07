#!/usr/bin/python3


class Rectangle:
    """define rectangle"""

    def __init__(self, width=0, height=0):
        """
        Args:
            param1 (width): width of square
            param2 (height): height of square
        """
        self.__width = width
        self.___height = height

        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        if width < 0:
            raise ValueError("width must be >= 0")


        if not isinstance(height, int):
            raise TypeError("height must be an integer")

        if height < 0:
            raise ValueError("height must be >= 0")



    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value


    @property
    def height(self):
        """getter for height"""
        return self.__height

    
    @height.setter
    def height(self, value):
        """setter for height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
 
