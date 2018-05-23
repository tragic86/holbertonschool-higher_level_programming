#!/usr/bin/python3
"""
funtion for square class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class defines Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ('[Square] ({:d}) {:d}/{:d} - {:d}'.format(
            self.id, self.x, self.y, self.width))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        new_list = ['id', 'size', 'x', 'y']
        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)
        for count, element in enumerate(args):
            setattr(self, new_list[count], element)

    def to_dictionary(self):
        a_dict = {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
            }
        return a_dict
