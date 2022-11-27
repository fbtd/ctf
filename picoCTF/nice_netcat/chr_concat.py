#!/usr/bin/env python3

import sys

def charify(file_in):
    for line in file_in:
        v = int(line)
        print(chr(v), end='')
    print()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as file_in:
            charify(file_in)
    else:
        charify(sys.stdin)
