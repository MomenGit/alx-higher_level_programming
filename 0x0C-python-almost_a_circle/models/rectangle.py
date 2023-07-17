#!/usr/bin/python3
"""Defines Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Define a rectangle object

    Args:
        width (int): The width of the rectangle
            must be > 0
        height (int): The height of the rectangle
            must be > 0
        x (int): The horizontal position of the rectangle
            (defaults to 0) must be >= 0
        y (int): The vertical position of the rectangle
            (defaults to 0) must be >= 0

    Attributes:
        width (int): The width of the rectangle
        height (int): The height of the rectangle
        x (int): The horizontal position of the rectangle
        y (int): The vertical position of the rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def area(self):
        """Calculates rectangle's area"""

        return self.__width * self.__height

    def display(self):
        """Returns an informal and nicely printable string representation
           of the rectangle instance, using print_symbol attribute.
           (Returns an empty string on height=0 or width=0)
        """
        print('\n'*self.y+'\n'.join([' '*self.x + '#' *
              self.width for i in range(self.height)]))

    def update(self, *args, **kwargs):
        """Update the class Rectangle that
        assigns an argument to each attribute
        or assigns a key/value argument to attributes
        """
        if args:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except Exception as e:
                pass
        else:
            for key, value in kwargs.items():
                if getattr(self, key) is not None:
                    setattr(self, key, value)

    def __str__(self):
        return "[{}] ({}) {}/{} - {}/{}".format(
            "Rectangle", self.id, self.x, self.y, self.__width, self.__height)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        self_dict = {}
        self_dict['x'] = self.x
        self_dict['y'] = self.y
        self_dict['id'] = self.id
        self_dict['height'] = self.height
        self_dict['width'] = self.width
        return self_dict

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, value: int) -> None:
        positive_validator("width", value)
        self.__width = value

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, value: int) -> None:
        positive_validator("height", value)
        self.__height = value

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, value: int) -> None:
        not_neg_validator("x", value)
        self.__x = value

    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, value: int) -> None:
        not_neg_validator("y", value)
        self.__y = value


def positive_validator(name, value):
    """Validates value must be an integer greater than 0"""

    if type(value) is not int:
        raise TypeError("{} must be an integer".format(name))
    if value <= 0:
        raise ValueError("{} must be > 0".format(name))


def not_neg_validator(name, value):
    """Validates value must be an integer greater than 0"""

    if type(value) is not int:
        raise TypeError("{} must be an integer".format(name))
    if value < 0:
        raise ValueError("{} must be >= 0".format(name))
