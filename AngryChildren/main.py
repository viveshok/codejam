#!/usr/bin/python3

import sys

if __name__ == "__main__":

    N = int(sys.stdin.readline())
    K = int(sys.stdin.readline())

    xs = sorted([int(X) for X in sys.stdin.readlines()])
    diffs = [xs[i+K-1]-xs[i] for i in range(N-K+1)]

    print(min(diffs))

