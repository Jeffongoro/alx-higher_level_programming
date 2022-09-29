#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mat_new = list(map(list, matrix))
    mat_new = [[x ** 2 for x in i] for i in mat_new]

    return mat_new
