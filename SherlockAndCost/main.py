#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
#import math
#import collections

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        N = int(sys.stdin.readline())

        BS = [int(X) for X in sys.stdin.readline().split()]

        CACHE = {(N-1, 1): 0, (N-1, BS[N-1]): 0}

        for i in range(N-2, -1, -1):
            CACHE[(i, 1)] = max(abs(1-BS[i+1])+CACHE[(i+1, BS[i+1])], CACHE[(i+1, 1)])
            CACHE[(i, BS[i])] = max(abs(1-BS[i])+CACHE[(i+1, 1)], abs(BS[i]-BS[i+1])+CACHE[(i+1, BS[i+1])])

        print(max(CACHE.values()))

