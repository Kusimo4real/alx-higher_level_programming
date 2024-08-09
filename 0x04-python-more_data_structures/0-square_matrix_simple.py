#!/usr/bin/python3

# a function that computes the square value of all integers of a matrix

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        squared_row = []
        for i in row:
            squared_row.append(i ** 2)
        new_matrix.append(squared_row)
    return new_matrix
