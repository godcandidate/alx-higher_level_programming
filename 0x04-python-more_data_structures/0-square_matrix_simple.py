#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    matrix_len = len(matrix)

    for i in range(matrix_len):
        new_matrix[i] = list(map(lambda x: x**2, matrix[i]))

    return (new_matrix)
