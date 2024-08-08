#!/usr/bin/python3
""" 0-prime_game """


def isWinner(x: int, nums: list[int]) -> str:
    """ Returns the winner of the PrimeGame """
    scores = {'Maria': 0, 'Ben': 0}
    for n in nums:
        if x == 0:
            break
        n_array = [i for i in range(1, n + 1)]
        essays = 0
        while n_array != [1]:
            prime = n_array[1]
            n_array = [i for i in n_array if i % prime != 0]
            essays += 1
        round_winner = 'Ben' if essays % 2 == 0 else 'Maria'
        scores[round_winner] += 1
        x -= 1
    if scores['Maria'] > scores['Ben']:
        return 'Maria'
    elif scores['Maria'] < scores['Ben']:
        return 'Ben'
    else:
        return None
