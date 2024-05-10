#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor can execute
"""


def minOperations(n):
    """
        In a text file, there is a single character H. Your text editor
    """
    if n < 2:
        return 0
    for op in range(2, n+1):
        if n % op == 0:
            return minOperations(int(n/op)) + op
