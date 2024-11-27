#!/usr/bin/python3
"""Coin Change problem
"""


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
    # custom miminum function
    def min_skip_none(a, b):
        if not a:
            return b
        if not b:
            return a
        return min(a, b)

    # internally memoized change maker function
    def memo_makeChange(coins, total, __cache={}):
        """Memoized makeChange function
        """
        if total in __cache:
            return __cache[total]
        if total == 0:
            min_coins = 0
        else:
            min_coins = None
            for coin in coins:
                # check for each coin and recursively
                # determine minimum coins for each path
                change_left = total - coin
                if change_left < 0:
                    continue
                next_min_coins = memo_makeChange(coins, change_left)
                if next_min_coins is None:
                    break
                min_coins = min_skip_none(min_coins,
                                          next_min_coins + 1)
        __cache[total] = min_coins
        return min_coins

    return memo_makeChange(coins, total) or -1
