#!/usr/bin/python3

"""
This module solves the N queens problem.
The N queens puzzle is the challenge of
placing N non-attacking queens on an N×N chessboard.
"""


import sys

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
