#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    items = a_dictionary.copy().items()

    for item in items:
        if item[1] == value:
            del a_dictionary[item[0]]
    return a_dictionary
