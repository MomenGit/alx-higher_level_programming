#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square shape object

    Args:
        size (int): The size of the square
    Attributes:
       size (int): The size of the square
            (defaults to 0 must be positive integer)
    """

    def __init__(self, size: int = 0):
        """Initialize Square"""

        self.__size = size

    def area(self):
        """Calculate the area of the square"""

        return self.__size**2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")
