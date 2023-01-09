#!/usr/bin/python
def uppercase(str):
    """Print string in uppercase."""
    for char in str:
        if ord(char) >= 97 and ord(char) <= 123:
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    else:
        print("")
