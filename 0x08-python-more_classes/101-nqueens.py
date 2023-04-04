#!/usr/bin/python3

"""
This module solves the N queens problem.
The N queens puzzle is the challenge of
placing N non-attacking queens on an N×N chessboard.
"""


import sys
"""
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

N = sys.argv[1]

if type(N) is not int:
    print("N must be a number")
    exit(1)
if N < 4:
    print("N must be at least 4")
    exit(1)

col = set()
pDiag = set() # (r+c)
nDiag = set() # (r-c)

res = []
board = [["."] * N for i in range(N)]

def backtrack(r):
    if r == N:
        copy = ["".join(row) for row in board]
        res.append(copy)
        return

    for c in range(N):
        if c in col or (r + c) in pDiag or (r - c) in nDiag:
            continue

        col.add(c)
        pDiag.add(r + c)
        nDiag.add(r - c)

        backtrack(r + 1)

        col.remove(c)
        pDiag.remove(r + c)
        nDial.remove(r - c)
        board[r][c] = "."
"""

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        exit(1)
