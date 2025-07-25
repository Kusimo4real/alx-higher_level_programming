#!/usr/bin/python3
"""
This module contain a function that divides all elements of a matrix
"""

def matrix_divided(matrix, div):
    """
    - Divides all elements of a matrix
    matrix must be a list of lists of integers or floats otherwise raise
    a type Error exception
    - Each row of the matric must be of the same size, otherwise  raise a type 
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix) or not (all(isinstance(num,(int, float)) for num in row) for row in matrix):
	    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not matrix:
	    return True
    row_length = len(matrix[0])
    for row in matrix:
	    if len(row) != row_length:
		    raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
	    raise TypeError("div must be a number")
    if div == 0:
	    raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
	    new_row = []
	    for num in row:
		    new_row.append(round(num / div, 2))
	    new_matrix.append(new_row)
    return new_matrix
