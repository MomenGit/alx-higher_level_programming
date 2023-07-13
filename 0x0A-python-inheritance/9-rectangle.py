#!/usr/bin/python3
"""Defines subclass Rectangle"""
mod = __import__("7-base_geometry")


class Rectangle(mod.BaseGeometry):
    """Represents a Rectangle Object

    Args:
        width (int): The width of the rectangle instance
        height (int): The height of the rectangle instance
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates rectangle's area"""

        return self.__width * self.__height

    def __str__(self):
        return "[{}] {}/{}".format(self.__class__.__name__,
                                   self.__width, self.__height)
