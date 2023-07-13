#!/usr/bin/python3
"""Defines Base class Geometry"""


class BaseGeometry:
    """Base class Geometry"""

    def area(self):
        """Raises an Exception with the message
        'area() is not implemented'"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value must be an integer greater than 0"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
