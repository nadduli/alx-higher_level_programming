#!/usr/bin/python3
for c in range(ord('a'), ord('z')):
    if c != ord('e') and c != ord('q'):
        print("{:c}".format(c), end="")
