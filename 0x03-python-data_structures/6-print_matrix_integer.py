#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for y in matrix:
            if y:
                for x in range(len(y)):
                    if x == len(y)-1:
                        print("{:d}".format(y[x]))
                    else:
                        print("{:d}".format(y[x]), end=" ")
            else:
                print("")
