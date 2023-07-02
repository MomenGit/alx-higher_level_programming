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

    def __init__(self, size=0):
        """Initialize Square"""

        self.size = size

    def area(self):
        """Calculate the area of the square"""

        return self.__size**2

    def my_print(self):
        """Print the square shape to the stdout"""

        if self.__size == 0:
            print()
        for i in range(0, self.__size):
            print('#'*self.__size)

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
