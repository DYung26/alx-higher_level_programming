#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for y in matrix:
            for x in range(len(y)):
                if x == len(y)-1:
                    print(y[x])
                else:
                    print(y[x], end=" ")
