#!/usr/bin/python3
import sys
if (len(sys.argv) != 1):
    print("{} arguments:".format(len(sys.argv) - 1))
else:
    print("0 argument.")
for i, sys.argv in enumerate(sys.argv[1:]):
    print(i+1, ":", sys.argv)
