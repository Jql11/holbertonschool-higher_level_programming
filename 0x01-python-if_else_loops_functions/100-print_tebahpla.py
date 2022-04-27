#!/usr/bin/python3
for i in range(123, 96, -1):
    if i % 2 == 0:
        print("{:c}".format(i), end='')
    else:
        print("{}".format(chr(i-32)), end='')
