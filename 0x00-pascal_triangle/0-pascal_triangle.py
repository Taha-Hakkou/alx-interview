#!/usr/bin/python3
""" 0-pascal_triangle """


def pascal_triangle(n):
    """ returns a list of lists of integers
    representing the Pascal’s triangle of n """
    pascal = []
    if n <= 0:
        return pascal
    pascal.append([1])
    if n == 1:
        return pascal
    nline = []
    for i in range(1, n + 1):
        nline = [nline[j] + nline[j - 1] for j in range(1, len(nline))]
        nline.append(1)
        nline.insert(0, 1)
        pascal.append(nline)
    return pascal
