#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
#import math
#import collections

SUPERGRID = list()
SUBGRID = list()

def is_subgrid(i, j, c):
    for row in SUBGRID:
        if row != SUPERGRID[i][j:j+c]:
            return False
        i += 1
    return True

def solve(R, r, C, c):
    for i in range(R-r+1):
        for j in range(C-c+1):
            if is_subgrid(i, j, c):
                return "YES"
    return "NO"

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        [R, C] = [int(X) for X in sys.stdin.readline().split()]

        SUPERGRID = list()
        for row in range(R):
            SUPERGRID.append(sys.stdin.readline().strip())

        [r, c] = [int(X) for X in sys.stdin.readline().split()]

        SUBGRID = list()
        for row in range(r):
            SUBGRID.append(sys.stdin.readline().strip())

        print(solve(R, r, C, c))

