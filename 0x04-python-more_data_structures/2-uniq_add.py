#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds all unique integers in a list"""
    unique_list = set(my_list)
    x = 0
    for i in unique_list:
        x += i
    return x
