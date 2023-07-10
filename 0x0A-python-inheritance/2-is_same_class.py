#!/usr/bin/python3
"""Define is_same_class function"""


def is_same_class(obj, a_class):
    """Return True if the object is exactly an instance of the specified class;
    otherwise False

    Args:
        obj: an object instance
        a_class: a class name
    """
    return type(obj) == a_class
