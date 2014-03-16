#!/usr/bin/python3

import sys

if __name__ == "__main__":

    N = int(sys.stdin.readline())

    xs = [int(X) for X in sys.stdin.readline().split()]

    [print(X, end=" ") for X in sorted(xs)]

