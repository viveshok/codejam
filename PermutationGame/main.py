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
def is_increasing(xs):
    if not xs:
        return True

    x0 = xs[0]
    for x in xs:
        if x < x0:
            return False
        x0 = x

    return True

@memoize
def is_winning_position(xs):
    if is_increasing(xs):
        return False

    return not all([is_winning_position(xs[:i]+xs[i+1:]) for i, _x in enumerate(xs)])

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        _N = int(sys.stdin.readline())

        xs = tuple([int(X) for X in sys.stdin.readline().split()])

        print("Alice" if is_winning_position(xs) else "Bob")

