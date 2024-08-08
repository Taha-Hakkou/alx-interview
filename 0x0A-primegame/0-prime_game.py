#!/usr/bin/python3
""" 0-prime_game """


def isWinner(x, nums):
    """ Returns the winner of the PrimeGame """
    if x < 1 or not nums:
        return None
    scores = {'Maria': 0, 'Ben': 0}
    for n in nums:
        n_array = [i + 1 for i in range(1, n)]
        essays = 0
        while n_array != []:
            prime = n_array[0]
            n_array = [i for i in n_array if i % prime != 0]
            essays += 1
        round_winner = 'Ben' if essays % 2 == 0 else 'Maria'
        scores[round_winner] += 1
    if scores['Maria'] == scores['Ben']:
        return None
    return 'Maria' if scores['Maria'] > scores['Ben'] else 'Ben'
