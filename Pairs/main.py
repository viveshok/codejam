#!/usr/bin/python3

import sys
import collections

if __name__ == "__main__":

    [N, K] = [int(X) for X in sys.stdin.readline().split()]

    count = 0
    tally = collections.defaultdict(int)
    for i in [int(X) for X in sys.stdin.readline().split()]:
        if i in tally:
            count += tally[i]

        tally[i+K] += 1
        tally[i-K] += 1

    print(count)

