#!/usr/bin/python3
def multiple_returns(sentence):
    """Returns a tuple with lenght of a string and it
    character
    """
    first = None
    if len(sentence):
        first = sentence[0]
    return (len(sentence), first)
