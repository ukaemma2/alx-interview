#!/usr/bin/python3
"""
    N-queen problem
    The next algo solve any N queen in any NxN
    Being N > 3
"""
import sys


def n_queen(temp_arr, arr, col, i, n):
    """
       n_queen - Find all posibles solution for N-queen problem and return it
             in a list
       @temp_arr: temporaly list to store the all points of a posible solution
       @arr: store all the solution
       @col: save a colum use for a queen
       @i: the row of the chess table
       @n: Number of queens
    """
    if (i > n):
        arr.append(temp_arr[:])
        return arr

    for j in range(n + 1):
        if i == 0 or ([i - 1, j - 1] not in temp_arr and
                      [i - 1, j + 1] not in temp_arr and
                      j not in col):
            if i > 1:
                dia = 0
                for k in range(2, i + 1):
                    if ([i - k, j - k] in temp_arr) or ([i - k, j + k] in temp_arr):
                        dia = 1
                        break
                if dia:
                    continue
            temp_arr.append([i, j])
            col.append(j)
            n_queen(temp_arr, arr, col, i + 1, n)
            col.pop()
            temp_arr.pop()

    return arr


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        n = int(sys.argv[1])
    except BaseException:
        print("N must be a number")
        exit(1)

    if not isinstance(n, int):
        print("N must be a number")
        exit(1)

    elif n < 4:
        print("N must be at least 4")
        exit(1)

    n_queen_arr = n_queen([], [], [], 0, n - 1)
    for i in n_queen_arr:
        print(i)
