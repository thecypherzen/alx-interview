#!/usr/bin/python3
"""Prime Game
"""


def get_primes(nums):
    """return prime numbers <= num
    """
    min_num, max_num = min(nums), max(nums)
    primes = [True for _ in range(max_num + 1)]
    numbers = [i for i in range(max_num + 1)]
    p = 2
    while (p * p <= max_num):
        if primes[p]:
            for i in range(p * p, max_num+1, p):
                primes[i] = False
        p += 1
    return [numbers[i] for i in range(2, max_num+1) if primes[i]]


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
    if not x <= 0 or not len(nums):
        return None
    players = {0: {"name": "Maria", "wins": 0},
               1: {"name": "Ben", "wins": 0}
               }
    primes = get_primes(nums)
    if not len(primes):
        return None
    for itr in range(x):
        nums_cpy = nums.copy()
        this_turn, next_turn = 0, 1
        array_bound = len(nums)
        deleted = float('-inf')
        for i in range(array_bound):
            if nums[i] in primes:
                # remove prime number and its multiples from array
                for j in range(array_bound):
                    if nums[j] > deleted and \
                       nums[j] != 1 and \
                       not nums[j] % nums[i]:
                        nums[j] = deleted
                this_turn = this_turn ^ next_turn
                next_turn = this_turn ^ next_turn
                this_turn = this_turn ^ next_turn
            else:
                pass
        players[next_turn]["wins"] = players[next_turn]["wins"] + 1
        nums = nums_cpy
    # extrapolate winner
    maria, ben = players[next_turn]["wins"], players[next_turn]["wins"]
    return players[0]["name"] if maria > ben else players[1]["name"]
