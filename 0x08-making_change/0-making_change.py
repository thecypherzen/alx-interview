#!/usr/bin/python3
"""Coin Change problem
"""


# custom miminum function
def min_skip_none(a, b):
    """Returns the minimum of two numbers ignoring None values
    """
    if not a:
        return b
    if not b:
        return a
    return min(a, b)


def changeMaker(coins, total, cache):
    """Calculates the min_coins for total recursively
    using a cache to memoize sub values
    """
    if total in cache:
        return cache[total]
    if total == 0:
        min_coins = 0
    else:
        min_coins = None
        for coin in coins:
            amount_left = total - coin
            if amount_left < 0:
                continue
            next_min_coins = changeMaker(coins, amount_left,
                                         cache)
            if next_min_coins is None:
                break
            min_coins = min_skip_none(min_coins,
                                      next_min_coins + 1)
        cache[total] = min_coins
    return min_coins


def makeChange(coins, total):
    """Determines the fewest number of coins needed to
    meet a given amount <total>.

    Params:
       - coins(obj:list): a list of coin values available.
         The value of a coin will always be an int > 0
       - total(number): the total change to give.

    Assumes:
       - There is an infinite number of coins for each denomination
         in our list.
    Returns:
       - 0 if total is <= 0
       - -1 if total cannot be met by any number of coins we have
    """
    if total < 0 or len(coins) == 0:
        return -1
    cache = {}
    min_coins = changeMaker(coins, total, cache)
    if min_coins is None:
        return -1
    return min_coins
