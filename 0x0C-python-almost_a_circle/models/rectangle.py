#!/usr/bin/python3
"""Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """
    Args:
    width
    height
    y
    x
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """initilzed"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """get area"""
        return (self.width * self.height)

    def display(self):
        """print instance"""
        print('\n' * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, end="")
            for j in range(self.width):
                print('#', end="")
            print()

    def __str__(self):
        """ return #
        """
        return("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".
               format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """update args and kwargs"""
        new_list = ['id', 'width', 'height', 'x', 'y']
        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)
        for count, element in enumerate(args):
            setattr(self, new_list[count], element)

    def to_dictionary(self):
        """get dict"""
        a_dict = {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
            }
        return a_dict
