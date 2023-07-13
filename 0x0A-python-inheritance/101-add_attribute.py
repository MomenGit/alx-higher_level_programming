#!/usr/bin/python3
"""Defines add_attribute function"""


def add_attribute(obj, attr_name, attr_value):
    """adds a new attribute to an object if it's possible"""

    if not hasattr(type(obj), "__slots__") and not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attr_name, attr_value)
