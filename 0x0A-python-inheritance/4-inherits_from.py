#!/usr/bin/python3
"""Defines inherits from function"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of
    a class that inherited (directly or indirectly)
    from the specified class; otherwise False

    Args:
        obj: An object instance
        a_class: obj class name
    """
    if type(obj) == a_class:
        return False

    return issubclass(type(obj), a_class)
