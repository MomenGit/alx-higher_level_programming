#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square shape object

    Args:
        __size (int): The size of the square
    Attributes:
        size (int): The size of the square
            (defaults to 0 must be positive integer)
        position (tuple(,)): The (x,y) position of the shape
            (defaults to (0,0) must be positive integers)
    """

    def __init__(self, size: int = 0, position: tuple = (0, 0)) -> None:
        """Initialize Square"""

        self.__position = position
        self.__size = size

    def area(self) -> int:
        """Calculate the area of the square"""

        return self.__size**2

    def my_print(self) -> None:
        """Print the square shape to the stdout"""

        if self.__size == 0:
            print()
            return
        for i in range(0, self.__position[1]):
            print()
        for i in range(0, self.__size):
            print("{}{}".format(' '*self.__position[0], '#'*self.__size))

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, value: int) -> None:
        if type(value) is int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self) -> tuple:
        return self.__position

    @position.setter
    def position(self, value: tuple):
        if type(value) is tuple:
            if len(value) == 2:
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
                    return
        raise TypeError(
            "position must be a tuple of 2 positive integers")
