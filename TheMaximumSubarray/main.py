#!/usr/bin/python3

import sys
#import math
#import collections

def solve(xs):
    """ find max sum of contiguous items
    >>> solve([5,-5,-4,0,3,-1])
    5
    >>> solve([-5])
    -5
    >>> solve([1,2,3,4,-1,-1,0,-5,2,2,2])
    10
    >>> solve([1,2,3,4,-1,-1,0,-5,2,8,2])
    15
    >>> solve([1,-1,-1])
    1
    >>> solve([1,-1,-1,9])
    9
    >>> solve([1,-1,-1,9,0,-5,2,4,2])
    12
    >>> solve([1,2,3,4,-1,-1,9,0,-5,0,0,1])
    17
    >>> solve([1,2,3,4,-1,-1,9,0,-5,2,4,2])
    20
    >>> solve([-1,-2,-3,-1,0,-1,-3,-3])
    0
    >>> solve([0,-1,-2,-3,-1,-1,-3,-3])
    0
    >>> solve([-1,-2,-3,-1,-1,-3,-3,0])
    0
    """
    best_streak = current_streak = xs[0]
    for i in range(1, len(xs)):
        current_streak = xs[i] + max(0, current_streak)
        best_streak = max(best_streak, current_streak)

    return best_streak


if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        _ = sys.stdin.readline()

        xs = [int(X) for X in sys.stdin.readline().split()]

        max_contiguous = solve(xs)

        positives = [x for x in xs if x>=0]
        if positives:
            max_non_contiguous = sum(positives)
        else:
            max_non_contiguous = max(xs)

        print(max_contiguous, " ", max_non_contiguous, sep="")

