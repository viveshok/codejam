#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
#import math
#import collections

if __name__ == "__main__":

    _N = int(sys.stdin.readline())

    A = [int(X) for X in sys.stdin.readline().split()]

    p = A[0]
    for a in A[1:]:
        p ^= a

    count = 0
    for a in A:
        count += 1 if a ^ p < a else 0

    print(count)

