#!/usr/bin/python3
"""Defines class LockedClass"""


class LockedClass:
    """class LockedClass with no class or object attribute,
    that prevents the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name"""

    def __setattr__(self, __name: str, __value: None) -> None:
        if __name == 'first_name':
            self.__dict__[__name] = __value
        else:
            raise AttributeError("'{}' object has no attribute '{}'".format(
                self.__class__.__name__, __name))
