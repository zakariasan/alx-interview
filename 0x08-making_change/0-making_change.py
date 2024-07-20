#!/usr/bin/python3
""" Make change for a given amount using specified coin denominations """


def makeChange(coin_denominations, target_amount):
    """
    Calculate the minimum number of coins needed to make up a given amount.

    Args:
        coin_denominations (List[int]): List of available coin denominations.
        target_amount (int): Total amount needed.

    Returns:
        int: Minimum number of coins needed, or -1 if the target
    """
    if target_amount <= 0:
        return 0

    num_coins = 0
    remaining_amount = target_amount

    coin_denominations.sort(reverse=True)

    for coin in coin_denominations:
        if remaining_amount == 0:
            break
        count = remaining_amount // coin
        num_coins += count
        remaining_amount -= count * coin

    return num_coins if remaining_amount == 0 else -1

