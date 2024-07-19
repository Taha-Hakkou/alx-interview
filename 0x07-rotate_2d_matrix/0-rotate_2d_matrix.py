#!/usr/bin/python3
""" 0-rotate_2d_matrix """


def rotate_2d_matrix(matrix):
    """ Rotates an n * n matrix 90 degrees clockwise """
    n = len(matrix)
    for i in range(n // 2):
        tmp = [matrix[j][n - 1 - i] for j in range(n - 2 - i, i - 1, -1)]
        for j in range(i, n - 1 - i):
            matrix[j][n - 1 - i] = matrix[i][j]
        tmp2 = matrix[n - 1 - i][1 + i: n - i]
        for j in range(1 + i, n - i):
            matrix[n - 1 - i][j] = tmp[j - i - 1]
        tmp = [matrix[j][i] for j in range(n - 1 - i, i, -1)]
        for j in range(1 + i, n - i):
            matrix[j][i] = tmp2[j - i - 1]
        for j in range(i, n - 1 - i):
            matrix[i][j] = tmp[j - i]
