#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        j = "".join(["{:d}" .format(j) for j in i])
        print (j)
