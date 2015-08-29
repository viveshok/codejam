#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
#import math
import collections

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    sticks = [int(X) for X in sys.stdin.readline().split()]
    counts = collections.Counter(sticks)
    sticks = sorted(counts.keys(), reverse=True)
    while sticks:
        print(N)
        N -= counts[sticks.pop()]

