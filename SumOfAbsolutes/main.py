#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
import itertools
#import math
#import collections

if __name__ == "__main__":

    [_N, Q] = [int(X) for X in sys.stdin.readline().split()]

    A = list(itertools.accumulate((int(X) for X in sys.stdin.readline().split())))

    A.insert(0, 0)

    for case in range(Q):

        [L, R] = [int(X) for X in sys.stdin.readline().split()]

        result = (A[R] - A[L-1]) % 2

        print("Odd" if result else "Even")

