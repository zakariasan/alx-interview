#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor can execute
"""


def minOperations(n):
    """
        In a text file, there is a single character H. Your text editor
    """
    if n <= 1:
        return 0
    operations = 0
    current_chars = 1
    while current_chars < n:
        if n % current_chars == 0:
            operations += 2  # Copy All and Paste
            current_chars *= 2
        else:
            divisor = find_largest_divisor(n)
            operations += divisor // current_chars + 1
            current_chars = divisor
    return operations


def find_largest_divisor(n):
    """ try to do it """
    for i in range(n // 2, 1, -1):
        if n % i == 0:
            return i
    return n
