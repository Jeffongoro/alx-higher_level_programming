#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("")
        return

    for i in matrix:
        for j in range(len(i)):
            print("{:d}".format(i[j]), end=("\n" if j == len(i) - 1 else " "))
