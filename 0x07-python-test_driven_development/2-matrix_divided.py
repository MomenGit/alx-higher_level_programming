#!/usr/bin/python3
def matrix_divided(matrix, div):
    new_matrix = []

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    validate_matrix(matrix)

    for row in matrix:
        new_matrix.append([])
        for e in row:
            new_matrix[-1].append(round(e/div, 2))

    return new_matrix


def validate_matrix(matrix):
    size = len(matrix[0])
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")
        for elem in row:
            if not isinstance(elem, int) and not isinstance(elem, float):
                raise TypeError(
                    "matrix must be a matrix "
                    "(list of lists) of integers/floats")
