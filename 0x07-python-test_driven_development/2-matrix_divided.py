#!/usr/bin/python3
"""
 a module that divides all elements of a matrix

"""
def matrix_divided(matrix, div):
    """a function that divide all elements of a matrix"""
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    first_row_length = len(matrix[0])

    for row in matrix:
        if len(row) != first_row_length:
            raise TypeError("Each row of the matrix must have the same size")
        if not isinstance(div, (int, float)):
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")
        return [[round(i / div, 2) for i in l] for l in matrix]

