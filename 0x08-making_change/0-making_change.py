#!/usr/bin/python3
"""
Main file for testing
"""


def makeChange(coins, amount):
    """
    How many of this type of coin can I get with my money? Okay,
        I'll take that many. Now, how much money do I have left?
        And how many coins do I have in my pocket?
    """
    if amount < 1:
        return 0
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if amount == 0:
            break
        num = amount // coin
        amount -= num * coin
        count += num
    return count if amount == 0 else -1
