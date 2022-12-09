#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        square_matrix = []
        for rows in matrix:
            square_matrix.append(list(map(lambda x: x**2, rows)))
            return (square_matrix)
