#!/usr/bin/python3
"""This script contains a function that creates the Pascal's triangle"""


def pascal_triangle(n):
    """Pascal's triangle function"""
    lst = [[1]]
    for i in range(1, n):
        row = [1] + [lst[i-1][j] + lst[i-1][j+1] for j in range(i-1)] + [1]
        lst.append(row)
    return lst if n > 0 else []
