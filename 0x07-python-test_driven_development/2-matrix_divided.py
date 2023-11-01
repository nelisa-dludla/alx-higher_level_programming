#!/usr/bin/python3
'''
This module includes one function, matrix_divided()
'''


def matrix_divided(matrix, div):
    '''
    Divides all elements of a matrix by a number

    Args:
        matrix (list of lists): The matrix to be divided. Each element should be an integer or float.
        div (int/float): The number to divide each element of the matrix by.

    Returns:
        list of lists: A new matrix with elements divided by the specified number.

    Raises:
        TypeError:
            If matrix is not a list of lists of integers/floats.
            If each row of the matrix does not have the same size.
            If div is not a number. (int or float)
        ZeroDivisionError:
            If div is zero
    '''

    if not isinstance(matrix, list):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    if isinstance(matrix[0], list):
        rowLength = len(matrix[0])

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

        if len(row) != rowLength:
            raise TypeError('Each row of the matrix must have the same size')

        for ele in row:
            if not isinstance(ele, (int, float)):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    newMatrix = []
    for row in matrix:
        newMatrix.append(list(map(lambda i: round(i / div, 2), row)))

    return newMatrix
