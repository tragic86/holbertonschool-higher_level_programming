#!/usr/bin/python3
"""
create a class
"""


class BaseGeometry:
    """Create class"""

    def area(self):

        """ raise Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """value validator"""

        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))

        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))

            """
            create a class
            """


class Rectangle(BaseGeometry):
    """inherit class"""

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
    """string class"""
    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
    """get area"""
    def area(self):
        return self.__width * self.__height


class Square(Rectangle):
    def __init__(self, size):
        super().integer_validator('size', size)
        self.__size = size
        super().__init__(self.__size, self.__size)
