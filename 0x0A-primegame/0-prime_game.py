#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor can execute
"""


def determine_winner(game_rounds, numbers):
    """Determine the winner of the prime game."""
    maria_wins = 0
    ben_wins = 0

    for number in numbers:
        rounds_list = list(range(1, number + 1))
        primes_list = get_primes_in_range(1, number)

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
            rounds_list.remove(smallest_prime)

            rounds_list = [n for n in rounds_list if n % smallest_prime != 0]

            maria_turn = not maria_turn

    if maria_wins > ben_wins:
        return "Winner: Maria"
    elif maria_wins < ben_wins:
        return "Winner: Ben"
    else:
        return None


def is_prime(n):
    """Returns True if n is prime, else False."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_primes_in_range(start, end):
    """Returns a list of prime numbers between start and end (inclusive)."""
    return [n for n in range(start, end + 1) if is_prime(n)]
