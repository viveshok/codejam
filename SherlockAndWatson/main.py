#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
#import math
#import collections

if __name__ == "__main__":

    [N, K, Q] = [int(X) for X in sys.stdin.readline().split()]

    Ns = [int(X) for X in sys.stdin.readline().split()]

    K %= N

    a = Ns[N-K:] + Ns[:N-K]

    for _case in range(Q):

        i = int(sys.stdin.readline())

        print(a[i])

