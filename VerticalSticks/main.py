#!/usr/bin/python3

import sys
import collections

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        N = int(sys.stdin.readline())
        sticks = [int(X) for X in sys.stdin.readline().split()]

        totals = collections.defaultdict(int)
        for stick in sticks:
            totals[stick] += 1

        acc = N
        cum_distn = dict()
        for k in sorted(totals.keys()):
            cum_distn[k] = acc
            acc -= totals[k]

        greater_or_equals = [cum_distn[stick] for stick in sticks]

        print("%0.2f" % sum([(N+1)/(k+1) for k in greater_or_equals]))

