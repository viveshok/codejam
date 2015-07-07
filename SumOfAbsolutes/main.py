#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
#import math
#import collections

if __name__ == "__main__":

    [_N, Q] = [int(X) for X in sys.stdin.readline().split()]

    A = [int(X)%2 for X in sys.stdin.readline().split()]

    for case in range(Q):

        [L, R] = [int(X) for X in sys.stdin.readline().split()]

        result = sum(A[L-1:R])

        print("Even" if result%2==0 else "Odd")

