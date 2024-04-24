#!/usr/bin/python3
"""
    returns a list of lists of integers representing the Pascal’s triangle
"""


def pascal_triangle(n):
    """
        Print the triangle
    """
    pascal = []
    if (n <= 0):
        return []
    for nbr in range(n):
        item = [1] * (nbr + 1)
        for x in range(1, nbr):
            item[x] = pascal[nbr - 1][x - 1] + pascal[nbr - 1][x]
        pascal.append(item)
    return pascal
