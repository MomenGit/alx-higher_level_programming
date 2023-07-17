#!/usr/bin/python3
"""Defines Rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Define a square object"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y)

    def __str__(self):
        return "[{}] ({}) {}/{} - {}".format(
            "Square", self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update the class Rectangle that
        assigns an argument to each attribute
        or assigns a key/value argument to attributes
        """
        if args:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[1]
                self.x = args[2]
                self.y = args[3]
            except Exception as e:
                pass
        else:
            for key, value in kwargs.items():
                if getattr(self, key) is not None:
                    if key == 'size':
                        setattr(self, 'width', value)
                        setattr(self, 'height', value)
                    else:
                        setattr(self, key, value)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
