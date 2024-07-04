#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor can execute
"""


def is_winner(x, nums):
    """
    Determines the winner of a set of prime number removal games.
       None.
    """
    if x <= 0 or nums is None or x != len(nums):
        return None

    max_num = max(nums)
    primes_sieve = generate_prime_sieve(max_num)

    ben_wins = 0
    maria_wins = 0

    for num in nums:
        prime_count = sum(primes_sieve[:num + 1])
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if ben_wins > maria_wins:
        return "Ben"
    elif maria_wins > ben_wins:
        return "Maria"
    else:
        return None


def generate_prime_sieve(n):
    """
    Generates a sieve of Eratosthenes up to n.
        is a prime number, and 0 otherwise.
    """
    sieve = [1] * (n + 1)
    sieve[0] = sieve[1] = 0

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i] == 1:
            for j in range(i * i, n + 1, i):
                sieve[j] = 0

    return sieve
