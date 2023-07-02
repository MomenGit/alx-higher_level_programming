#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square shape object

    Args:
        size (int): The size of the square
    """

    def __init__(self, size=0):
        """Initialize Square"""

        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
        self.__size = size

    def area(self):
        """Calculate the area of the square"""

        return self.__size**2
