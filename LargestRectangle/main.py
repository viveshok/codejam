#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
#import math
#import collections

def solve(buildings, N):
    min_height, idx = min((height, idx) for (idx, height) in enumerate(buildings))
    current_area = N*min_height
    left_area = solve(buildings[:idx], idx) if idx else 0
    right_area = solve(buildings[idx+1:], N-idx-1) if idx<N-1 else 0
    return max(left_area, current_area, right_area)

if __name__ == "__main__":

    N = int(sys.stdin.readline())

    buildings = [int(X) for X in sys.stdin.readline().split()]

    print(solve(buildings, N))

