#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
import math
#import collections

def solve(L, R):
    """
    >>> solve(10, 15)
    7
    >>> solve(17, 23)
    7
    >>> solve(2, 17)
    31
    >>> solve(5, 5)
    0
    """
    if L == R:
        return 0

    l = int(math.log(L, 2))
    r = int(math.log(R, 2))
    while l == r:
        L -= 2**l
        R -= 2**r
        l = int(math.log(L, 2)) if L else 0
        r = int(math.log(R, 2))

    return 2**(r+1)-1

if __name__ == "__main__":

    L = int(sys.stdin.readline())
    R = int(sys.stdin.readline())

    print(solve(L, R))

