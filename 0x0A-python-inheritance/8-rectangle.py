#!/usr/bin/python3
"""Defines subclass Rectangle"""
mod = __import__("7-base_geometry")


class Rectangle(mod.BaseGeometry):
    """Represents a Rectangle Object"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
