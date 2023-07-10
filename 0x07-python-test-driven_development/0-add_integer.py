#!/usr/bin/python3
""" 
Defines an add function 
Adds integers of floats
otherwise raises TypeError exception
"""


def add_integer(a, b=98):
    """Adds two integers
        a and b must be integers or floats, otherwise raise a TypeError
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


if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/0-add_integer.txt", verbose=True)
