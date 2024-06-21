#!/usr/bin/python3
""" make me happy """


def makeChange(coin_denominations, target_amount):
    """
        coin_denominations (List[int]): List of coin denominations available
        target_amount (int): Total amount needed
    """
    if target_amount <= 0:
        return 0

    min_coins = [float('inf')] * (target_amount + 1)
    min_coins[0] = 0

    # Fill the DP array
    for coin in coin_denominations:
        for amount in range(coin, target_amount + 1):
            if min_coins[amount - coin] != float('inf'):
                min_coins[amount] = min(
                    min_coins[amount], min_coins[amount - coin] + 1)

    result = min_coins[target_amount]
    return result if result != float('inf') else -1
