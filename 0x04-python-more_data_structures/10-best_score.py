#!/usr/bin/python3
def best_score(a_dictionary):
    """function that returns a key with the biggest integer value."""
    bvalue = 0
    bkey = None
    if not bool(a_dictionary):
        return bkey
    for k, v in a_dictionary.items():
        bkey = k if v > bvalue else bkey
        bvalue = max(bvalue, v)
    return bkey
