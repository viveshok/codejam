#!/usr/bin/python3

import sys

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

    if N < 0:
        return 0
    if N == 0:
        return 1

    (A, B, C, D) = coins 

    if A>0:
        num_solns = solve(N-1, (A-1, B, C, D))
        num_solns += solve(N, (0, B, C, D))
        return num_solns

    if B>0:
        num_solns = solve(N-2, (A, B-1, C, D))
        num_solns += solve(N, (A, 0, C, D))
        return num_solns

    if C>0:
        num_solns = solve(N-5, (A, B, C-1, D))
        num_solns += solve(N, (A, B, 0, D))
        return num_solns

    if D>0:
        num_solns = solve(N-10, (A, B, C, D-1))
        num_solns += solve(N, (A, B, C, 0))
        return num_solns

    return 0

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        N = int(sys.stdin.readline())

        coins = (int(X) for X in sys.stdin.readline().split())

        print(solve(N, coins))

