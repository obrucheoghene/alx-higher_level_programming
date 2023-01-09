#!/usr/bin/python3
for digit in range(10):
    for second_digit in range(digit + 1, 10):
        if digit == 8 and second_digit == 9:
            print("{}{}".format(digit, second_digit))
        else:
            print("{}{}".format(digit, second_digit), end=", ")
