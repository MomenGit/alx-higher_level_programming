#!/usr/bin/python3
"""Defines find_peak function"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    if list_of_integers == [] or type(list_of_integers) is not list:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
