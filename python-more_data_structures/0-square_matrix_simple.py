#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = list([])
    r = 0
    for row in matrix:
        new_row = list([])
        for n in row:
            r = n**2
            new_row.append(r)
        new_matrix.extend([new_row])
    return new_matrix
