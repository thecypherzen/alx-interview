#!/usr/bin/env python3
"""Test for minimum coins problem
"""
import time

makeChange = __import__('0-making_change').makeChange

beforeA = time.time()
changeA = makeChange([1, 2, 25], 37)
afterA = time.time()
print(f"changeA: {changeA}, TIME: {afterA - beforeA:.6f}")

beforeB = time.time()
changeB = makeChange([1256, 54, 48, 16, 102], 1453)
afterB = time.time()
print(f"changeB: {changeB}, TIME: {afterB - beforeB:6f}")
