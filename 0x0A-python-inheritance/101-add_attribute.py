#!/usr/bin/python3
"""Defines add_attribute function"""


def add_attribute(obj, attr_name, attr_value):
    """Adds a new attribute to an object if it's possible

    Args:
        obj (Any): An object
        attr_name (string): Attribute name
        attr_value (Any): Attribute value
    """

    if not hasattr(type(obj), "__slots__") and not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attr_name, attr_value)
