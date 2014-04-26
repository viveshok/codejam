#!/usr/bin/python3

import sys

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        N = int(sys.stdin.readline())
        sticks = sorted([int(X) for X in sys.stdin.readline().split()])

        print(sticks)

