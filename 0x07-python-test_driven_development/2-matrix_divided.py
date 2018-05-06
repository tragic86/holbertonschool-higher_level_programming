#!/usr/bin/python3
"""
Function to divide matrix


"""


def matrix_divided(matrix, div):
    """loop through matrix"""
    for row in matrix:
        for colum in row:

            if type(matrix) is not list:
                raise TypeError("matrix must be a matrix"
                                "(list of lists) of integers/floats")
                for i in range(len(matrix)):
                    for j in range(len(matrix[i])):
                        if type(matrix) is not int:
                            raise TypeError("matrix must be a matrix"
                                            "(list of lists)"
                                            "of integers/floats")
                        if type(matrix) is not float:
                            raise TypeError("matrix must be a matrix"
                                            "(list of lists)"
                                            "of integers/floats")
                        if len(matrix[i][j] == matrix[i][j] + 1):
                            raise TypeError("Each row of the matrix"
                                            "must have the same size")

            if div == 0:
                raise ZeroDivisionError("division by zero")
    return [[round(colum/div, 2)for colum in row]for row in matrix]
