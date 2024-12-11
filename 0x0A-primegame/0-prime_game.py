#!/usr/bin/python3
"""Prime Game
"""


def get_primes(num):
    """return prime numbers <= num
    """
    primes = [True for _ in range(num + 1)]
    numbers = [i for i in range(num + 1)]
    p = 2
    while (p * p <= num):
        if primes[p]:
            for i in range(p * p, num+1, p):
                primes[i] = False
        p += 1
    return [numbers[i] for i in range(2, num+1) if primes[i]]


def isWinner(x, nums):
    """Determines winner of prime game
    Solution:
    => set turn of Maria to 0 and that of Ben to 1
    => for each game session:
       => iterate through the numbers and pick first prime number
       => if no prime number is found, return next turn as winner
       => filter out all multiples of current prime number
       => set array to filtered array
    """
    players = {0: {"name": "Maria", "wins": 0},
               1: {"name": "Ben", "wins": 0}
               }
    for num in nums:
        numbers, primes = list(range(1, num + 1)), get_primes(num)
        if not primes or not nums:
            return None
        numbers_cpy, array_bound = numbers.copy(), len(numbers)
        this_turn, next_turn = 0, 1
        deleted = float('-inf')
        for i in range(array_bound):
            if numbers[i] in primes:
                # remove prime number and its multiples from array
                for j in range(array_bound):
                    if numbers[j] > deleted and \
                       numbers[j] != 1 and \
                       not numbers[j] % numbers[i]:
                        numbers[j] = deleted
                # change turns
                this_turn = this_turn ^ next_turn
                next_turn = this_turn ^ next_turn
                this_turn = this_turn ^ next_turn
            else:
                pass
        players[next_turn]["wins"] = players[next_turn]["wins"] + 1
        numbers = numbers_cpy
    # determine winner
    maria, ben = players[0]["wins"], players[1]["wins"]
    if maria == ben:
        return None
    if maria > ben:
        return players[0]["name"]
    else:
        return players[1]["name"]
