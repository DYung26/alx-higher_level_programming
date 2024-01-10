#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return ([[(x[i] ** 2) for i in range(len(matrix))] for x in matrix])
