#!/usr/bin/env python3
""" 0-minoperations """


def minOperations(n: int) -> int:
    """ calculates the fewest number of operations needed
    to result in exactly n H characters in the file """
    if n <= 1:
        return 0
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            break
    if i == 1:
        return n
    else:
        return (n // i) + minOperations(i)
