#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor can execute
"""


def isWinner(x, nums):
    """
    Determines the winner of a set of prime number removal games.

    Args:
        x (int): The number of rounds.
        nums (list of int): A list of integers where each integer n denotes
        a set of consecutive integers starting from 1 up to and including n.

    Returns:
        str: The name of the player who won the most rounds (either "Ben"
        or "Maria").
        None: If the winner cannot be determined.

    Raises:
        None.
    """
    if x <= 0 or nums is None or x != len(nums):
        return None  # Check for invalid input

    max_num = max(nums)
    # Generate prime sieve up to max_num
    primes_sieve = generate_prime_sieve(max_num)

    ben_wins = 0
    maria_wins = 0

    for num in nums:
        prime_count = sum(primes_sieve[:num + 1])  # Count primes up to num
        if prime_count % 2 == 0:
            ben_wins += 1  # Ben wins if the count of primes is even
        else:
            maria_wins += 1  # Maria wins if the count of primes is odd

    if ben_wins > maria_wins:
        return "Ben"
    elif maria_wins > ben_wins:
        return "Maria"
    else:
        return None


def generate_prime_sieve(n):
    """
    Generates a sieve of Eratosthenes up to n.

    Args:
        n (int): The maximum number to check for primality.

    Returns:
        list of int: A list where the value at each index is 1 if the index
        is a prime number, and 0 otherwise.
    """
    sieve = [1] * (n + 1)  # Initialize sieve with 1s
    sieve[0] = sieve[1] = 0  # 0 and 1 are not prime numbers

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i] == 1:
            for j in range(i * i, n + 1, i):
                sieve[j] = 0  # Mark multiples of i as non-prime

    return sieve
