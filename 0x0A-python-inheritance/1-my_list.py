#!/usr/bin/python3
"""Module defines a class that inherits from list."""


class MyList(list):
    """Prints sorted ascending list"""

    def print_sorted(self):
        """Print sorted ascending list"""
        print(sorted(self))
