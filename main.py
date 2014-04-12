#!/usr/bin/python3

import sys

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        [N, C] = [int(X) for X in sys.stdin.readline().split()]

        Ans = N + C

        print("Case #", case+1, ": ", Ans, sep="")

