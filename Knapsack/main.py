#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
#import math
#import collections

sys.setrecursionlimit(10000)

def memoize(function):
    cache = dict()
    def memoized_function(*args):
        if args in cache:
            return cache[args]
        else:
            result = function(*args)
            cache[args] = result
            return result
    return memoized_function

@memoize
def solve(n, A):
    if n == 0:
        return n
    current_soln = n
    for a in A:
        if n >= a:
            current_soln = min(current_soln, solve(n-a, A))
    return current_soln

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        [_n, k] = [int(X) for X in sys.stdin.readline().split()]

        A = frozenset([int(X) for X in sys.stdin.readline().split()])

        print(k-solve(k, A))

