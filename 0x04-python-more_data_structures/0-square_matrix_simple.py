#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return ([[(x[i] ** 2) for i in range(len(x))] for x in matrix])
