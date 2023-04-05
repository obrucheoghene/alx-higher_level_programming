#!/usr/bin/python3

"""
The LockedClass module
"""


class LockedClass:

    __slots__ = ['first_name']

    def __setattr__(self, name, value):
        if not hasattr(self, 'first_name') and name != 'first_name':
            raise AttributeError
        super().__setattr__(name, value)
