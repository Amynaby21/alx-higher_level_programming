#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = list(map(lambda x:x*x)) for list in matrix
    return (square_matrix)
