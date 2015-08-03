#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
#import math
#import collections

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
def solve(N, coins):
    if N == 0:
        return 1
    if N < 0 or not coins:
        return 0
    return solve(N-coins[0], coins) + solve(N, coins[1:])

if __name__ == "__main__":

    [N, _M] = [int(X) for X in sys.stdin.readline().split()]
    coins = tuple([int(X) for X in sys.stdin.readline().split()])

    print(solve(N, coins))

