#!/usr/bin/python3
"""Defines pascal_triangle function"""


def pascal_triangle(n):
    """Returns a list of lists of integers
    representing the Pascal's triangle of n
    """
    pascal = []

    if n <= 0:
        return pascal

    pascal.append([1])
    for i in range(1, n):
        pascal.append([1])
        for j in range(1, i):
            pascal[i].append(pascal[i-1][j-1]+pascal[i-1][j])
        pascal[i].append(1)
    return pascal
