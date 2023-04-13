#!/usr/bin/python3
"""
This module defines a Pascal's Triangle function.
"""


def pascal_triangle(n):
    """
    Defines Pascal's Triangle of size n.
    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri_base = triangles[-1]
        new = [1]
        for i in range(len(tri_base) - 1):
            new.append(tri_base[i] + tri_base[i + 1])
        new.append(1)
        triangles.append(new)
    return triangles
