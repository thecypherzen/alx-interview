#!/usr/bin/env python3
"""Test for minimum coins problem
"""
import time

makeChange = __import__('0-making_change').makeChange
before = time.time()
coins, total = [1, 4, 5], 13
print(f"coins: {coins}, total: {total}")
change = makeChange(coins, total)
after = time.time()
print(f"  {change} ({(after - before):.6f}s)")

print('++++++++++++++++++++++++++++')

coins, total = [1, 4, 5], 150
print(f"coins: {coins}, total: {total}")
before = time.time()
change = makeChange(coins, total)
after = time.time()
print(f"  {change} ({(after - before):.6f}s)")
print('++++++++++++++++++++++++++++')

coins, total = [1, 2, 25], 37
print(f"coins: {coins}, total: {total}")
before = time.time()
change = makeChange(coins, total)
after = time.time()
print(f"  {change} ({(after - before):.6f}s)")
print('++++++++++++++++++++++++++++')

coins, total = [1256, 54, 48, 16, 102], 1453
print(f"coins: {coins}, total: {total}")
before = time.time()
change = makeChange(coins, total)
after = time.time()
print(f"  {change} ({(after - before):.6f}s)")
