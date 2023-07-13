#!/usr/bin/python3
"""Defines Base class Geometry"""


class BaseGeometry:
    """Base class Geometry"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value must be an integer greater than 0"""

        if isinstance(value, int):
            if value <= 0:
                raise ValueError("{} must be greater than 0".format(name))
            else:
                self.__size = value
        else:
            raise TypeError("{} must be an integer".format(name))
