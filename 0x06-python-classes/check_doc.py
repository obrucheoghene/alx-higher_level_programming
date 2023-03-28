#!/usr/bin/python3
import sys

if (len(sys.argv) != 2):
    print("Wrong command. Useage: ./check_doc <hame_of_module>")
    exit()
module = sys.argv[1]

doc = __import__(module).__doc__

if (doc is None):
    print("No documentation")
else:
    print(doc)
