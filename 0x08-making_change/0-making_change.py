#!/usr/bin/python3
""" 0-making_change """


def makeChange(coins, total):
    """Returns the fewest number of coins needed to meet total"""
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    coins_number = 0
    for coin in coins:
        coins_number += (total // coin)
        total %= coin
    if total == 0:
        return coins_number
    return -1
