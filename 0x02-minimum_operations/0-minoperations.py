#!/usr/bin/python3
""" 0-minoperations """


def minOperations(n: int) -> int:
    """ calculates the fewest number of operations needed
    to result in exactly n H characters in the file """
    if n < 2:
        return 0
    i = n
    for j in range(2, n // 2):
        if n % j == 0:
            i = j
            break
    if i == n:
        return n
    else:
        return (i) + minOperations(n // i)
