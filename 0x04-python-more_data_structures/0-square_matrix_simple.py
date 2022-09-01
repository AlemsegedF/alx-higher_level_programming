#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    k = j = 0
    for row in matrix:
        new.append(row.copy())
    for row in new:
        for i in row:
            row[row.index(i)] = i ** 2
            j += 1
        k += 1
    return new
