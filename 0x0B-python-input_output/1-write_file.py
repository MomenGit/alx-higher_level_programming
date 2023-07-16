#!/usr/bin/python3
"""Define write_file function"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and
    returns the number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as file:
        written = file.write(text)
    return written
