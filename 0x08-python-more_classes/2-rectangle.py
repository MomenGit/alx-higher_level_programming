#!/usr/bin/python3
"""Defines a rectangle class"""


class Rectangle:
    """Represents a rectangle object class

    Args:
        width (int): The width of the rectangle
            (defaults to 0) must be greater than or equal to 0
        height (int): The height of the rectangle
            (defaults to 0) must be greater than or equal to 0

    Attributes:
        width (int): The width of the rectangle
        height (int): The height of the rectangle
    """

    def __init__(self, width: int = 0, height: int = 0) -> None:
        self.height = height
        self.width = width

    def area(self):
        """Calculate the rectangle instance's area"""
        return self.height * self.width

    def perimeter(self):
        """Calculate the rectangle instance's perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2*self.height + 2*self.width

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, value: int) -> None:
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, value: int) -> None:
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
