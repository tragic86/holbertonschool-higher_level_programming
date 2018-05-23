#!/usr/bin/python3


from models.base import Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        return (self.width * self.height)

    def display(self):
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
        new_list = ['id', 'width', 'height', 'x', 'y']
        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)
        for count, element in enumerate(args):
            setattr(self, new_list[count], element)

    def to_dictionary(self):
        a_dict = {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
            }
        return a_dict
