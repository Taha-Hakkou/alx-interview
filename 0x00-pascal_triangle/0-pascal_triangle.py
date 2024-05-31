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
    level = []
    for i in range(1, n):
        level = [level[j] + level[j - 1] for j in range(1, len(level))]
        level.append(1)
        level.insert(0, 1)
        pascal.append(level)
    return pascal
