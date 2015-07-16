#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
#import math
import collections

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        _N = int(sys.stdin.readline())

        As = [int(X) for X in sys.stdin.readline().split()]

        cache = collections.defaultdict(int)
        for A in As:
            cache[A] += 1

        print(sum([n*(n-1) for n in cache.values()]))

