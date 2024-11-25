#!/usr/bin/python3
"""Pascal's Triangle
"""


def pascal_triangle(n):
    """Returns a list of lists representing
    Pascal's triangle from 1 to n

    Params:
      n(int): the order of the pascal's triangle

    Expects:
      - n to be an integer

    Returns:
      - List of list of Pascal's triangle numbers if n > 0
      - An empty list if n <= 0
    """
    res = []
    if n <= 0:
        return res

    # inner function to generate each new row
    def generate(num, _cache={}):
        if num == 1:
            _cache[num - 1] = [1]
        # use cached row if it exists
        if num - 1 in _cache:
            return _cache[num - 1]
        # generate new row if it doesn't exist
        count, total, row, prev = 0, 0, [], res[num - 2]
        slow, fast = -1, 0  # indices of elements to add next
        for n in range(num - 1):
            if slow < 0:
                total = 0 + prev[fast]
            else:
                total = prev[slow] + prev[fast]
            row.insert(n, total)
            count += 1
            if count != num:
                row.insert(n+1, total)
                count += 1
            if count == num:
                break
            slow, fast = fast, fast + 1
        # save new row in cache
        _cache[num - 1] = row
        return row

    for i in range(1, n + 1):
        res.append(generate(i))
    return res
