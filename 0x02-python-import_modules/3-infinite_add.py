#!/usr/bin/python3
from sys import argv, exit

if __name__ != "__main__":
    exit()

sum = 0

for i in range(1, len(argv)):
    sum += int(argv[i])
else:
    print("{:d}".format(sum))
