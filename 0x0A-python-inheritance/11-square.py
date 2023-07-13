#!/usr/bin/python3
"""Defines subclass Square"""
mod = __import__("9-rectangle")


class Square(mod.Rectangle):
    """Represents a Square Object

    Args:
        size (int): The size of the square instance
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculate square's instance area"""

        return self.__size**2

    def __str__(self):
        return "[{0}] {1}/{1}".format("Square", self.__size)
