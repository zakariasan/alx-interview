#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor can execute
"""


def is_winner(x, nums):
    """Determine the overall winner after x rounds of the prime game."""
    def is_prime(n):
        """Returns True if n is prime, else False."""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_primes_in_range(start, end):
        """Returns a list of prime numbers between start"""
        return [n for n in range(start, end + 1) if is_prime(n)]

    maria_wins = 0
    ben_wins = 0

    for num in nums:
        rounds_list = list(range(1, num + 1))
        primes_list = get_primes_in_range(1, num)

        if not primes_list:
            ben_wins += 1
            continue

        maria_turn = True

        while True:
            if not primes_list:
                if maria_turn:
                    ben_wins += 1
                else:
                    maria_wins += 1
                break

            smallest_prime = primes_list.pop(0)
            rounds_list = [n for n in rounds_list if n % smallest_prime != 0]
            primes_list = [p for p in primes_list if p in rounds_list]

            maria_turn = not maria_turn

    if maria_wins > ben_wins:
        return "Winner: Maria"
    elif ben_wins > maria_wins:
        return "Winner: Ben"
    else:
        return None


print("Winner:", is_winner(5, [2, 5, 1, 4, 3]))
