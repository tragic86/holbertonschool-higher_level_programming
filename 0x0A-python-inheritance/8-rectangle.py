#!/usr/bin/python3
"""
create a class
"""


class BaseGeometry:
    """Create class"""

    def area(self):
        """
        raise error
        """
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
