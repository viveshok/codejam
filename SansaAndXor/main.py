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

        _N = sys.stdin.readline()

        xs = [int(X) for X in sys.stdin.readline().split()]

        if len(xs) % 2:
            result = 0;
            for x in [x for (i, x) in enumerate(xs) if not i%2]:
                result ^= x
            print(result)
        else:
            print(0)

