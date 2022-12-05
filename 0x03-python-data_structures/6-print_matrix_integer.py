#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for part in matrix:
        for i in range(len(part)):
            print("{:d}".format(part[i]), end="")
            if i is not len(part) - 1:
                print(" ", end="")
        print("")
