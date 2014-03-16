#!/usr/bin/python3

import sys

if __name__ == "__main__":

    [N, K] = [int(X) for X in sys.stdin.readline().split()]

    cs = sorted([int(X) for X in sys.stdin.readline().split()], reverse=True)
    multipliers = [i//K+1 for i in range(N)]

    print(sum([i*j for i,j in zip(cs, multipliers)]))

