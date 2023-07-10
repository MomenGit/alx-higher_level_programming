#!/usr/bin/python3
""" Defines an add function """


def add_integer(a, b=98):
    """Adds two integers

    Args:
        a (int|float): first number
        b (int|float): second number

    Raises:
        TypeError: If a or b aren't instances of int or float
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    else:
        a = int(a)
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    else:
        b = int(b)
    return a + b
