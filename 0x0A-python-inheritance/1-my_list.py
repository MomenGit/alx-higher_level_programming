#!/usr/bin/python3
"""Defines class MyList"""


class MyList(list):
    """A subclass of list"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        shallow_copy = self[:]
        shallow_copy.sort()
        print(shallow_copy)
