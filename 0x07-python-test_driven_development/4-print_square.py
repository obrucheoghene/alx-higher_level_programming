#!/usr/bin/python3

"""
The module describes a function print_square that prints square
wit the character #
"""


def print_square(size):
    """
    This function prints a square with the character #.

    Args:
        size (int): The size of the integer.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than zero.
    """

    if size is None or not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    output = ''
    for i in range(size):
        if i == size - 1:
            output += "#" * size
        else:
            output += "#" * size + "\n"
    print(output)
