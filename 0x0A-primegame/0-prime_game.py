#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor can execute
"""


def isWinner(x, nums):
    def sieve(n):
        """ Returns a list of prime numbers up to n using the Sieve of Eratosthenes """
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if (is_prime[p] == True):
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        primes = [p for p in range(2, n + 1) if is_prime[p]]
        return primes

    if not nums or x < 1:
        return None

    max_num = max(nums)
    primes = sieve(max_num)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_count = 0
        for prime in primes:
            if prime > n:
                break
            primes_count += 1

        # Determine winner
        if primes_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


# Example usage
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
