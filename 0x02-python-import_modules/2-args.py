#!/usr/bin/python3
import sys

if __name__ != "__main__":
    sys.exit()

if len(sys.argv) == 1:
    print("{:d} arguments.".format(0))
elif len(sys.argv) == 2:
   print("{:d} argument:".format(1))
   print("{:d}: {}".format(1, sys.argv[1]))
else:
    print("{:d} arguments:".format(len(sys.argv) - 1))
    for i in range(1, len(sys.argv)):
        print("{:d}: {}".format(i, sys.argv[i]))
