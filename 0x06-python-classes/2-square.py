#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square shape object

    Args:
        size (int): The size of the square
    """

    def __init__(self, size: int = 0) -> None:
        """Initialize Square"""

        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
        self.__size = size
