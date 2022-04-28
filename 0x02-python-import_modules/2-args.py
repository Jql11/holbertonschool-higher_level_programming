#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if (len(sys.argv) == 1):
        print("0 argument.")
    elif (len(sys.argv) == 2):
        print("1 argument:")
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
    for i, sys.argv in enumerate(sys.argv[1:]):
        print(f"{i+1}: {sys.argv}")
