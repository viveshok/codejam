#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
#import math
import collections

def solve(cs):

    counts = collections.defaultdict(int)
    for c in cs:
        counts[c] += 1
    num_pickables = collections.defaultdict(int)
    cum_sum = 0
    for i in range(50001):
        cum_sum += counts[i]
        num_pickables[i] = cum_sum

    num_picked = 0
    num_cards_remaining = len(cs)
    solution = 1
    
    while num_cards_remaining:
        num_pickable = num_pickables[num_picked] - num_picked
        if num_pickable:
            solution = (solution * num_pickable) % 1000000007
            num_cards_remaining -= 1
            num_picked += 1
        else:
            return 0

    return solution

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        _ = sys.stdin.readline()
        cs = [int(X) for X in sys.stdin.readline().split()]

        soln = solve(cs)

        print(soln, sep="")

