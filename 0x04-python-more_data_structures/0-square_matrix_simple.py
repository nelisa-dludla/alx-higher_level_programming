#!/usr/bin/python3
'''
This function computes the sqaure value of all inteegrs of a matrix
'''


def square_matrix_simple(matrix=[]):
    newMatrix = []

    for row in matrix:
        newMatrix.append(list(map(lambda i: i ** 2, row)))

    return newMatrix
