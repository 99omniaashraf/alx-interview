#!/usr/bin/python3
"""
    Prime Game
"""


def isWinner(x, nums):
    """Determine the winner of the Prime Game"""
    if x <= 0 or not nums:
        return None
    if x != len(nums):
        return None

    ben = 0
    maria = 0

    max_num = max(nums)
    is_prime = [True] * (max_num + 1)
    is_prime[0], is_prime[1] = False, False

    for i in range(2, int(max_num**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_num + 1, i):
                is_prime[j] = False

    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)

    for n in nums:
        if prime_count[n] % 2 == 0:
            ben += 1
        else:
            maria += 1

    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None
