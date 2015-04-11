#!/usr/bin/python3

import sys
#import math
#import collections

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        (X, R, C) = (int(X) for X in sys.stdin.readline().split())

        if (R*C)%X != 0:
            ans = "RICHARD"
        elif X >= 7:
            ans = "RICHARD"
        elif X <= 2:
            ans = "GABRIEL"
        elif X >= 2*min(R, C):
            ans = "RICHARD"
        else:
            ans = "GABRIEL"

        print("Case #", case+1, ": ", ans, sep="")

