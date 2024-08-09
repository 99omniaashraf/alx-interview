#!/usr/bin/python3
"""
Module 0-prime_game
"""


def isWinner(x, nums):
    def sieve(n):
        """ Returns a list of primes up to and including n """
        is_prime = [True] * (n + 1)
        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, n + 1) if is_prime[p]]

    def play_game(n):
        """ Determine the winner of the game with parameter n """
        primes = sieve(n)
        if not primes:
            return "Ben"  # If no primes, Maria can't make a move, so Ben wins.

        # Count the number of primes up to n
        total_primes = len(primes)

        # If total number of primes is odd, Maria (the first player) wins
        # If total number of primes is even, Ben (the second player) wins
        return "Maria" if total_primes % 2 == 1 else "Ben"

    # Count the wins for each player
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
