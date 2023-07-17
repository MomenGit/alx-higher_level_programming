#!/usr/bin/python3
"""Defines class_to_json function"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object
    """
    dict_repr = {}
    attributes = obj.__dict__

    for attr, value in attributes.items():
        if isinstance(value, (list, dict, str, int, bool)):
            dict_repr[attr] = value

    return dict_repr
