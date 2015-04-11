#!/usr/bin/python3

import sys
#import math
#import collections

def solve(ss):
    answer = 0
    cumsum = 0
    for (idx, s) in enumerate(ss):
        if s > 0 and cumsum < idx:
            required = idx-cumsum
            answer += required
            cumsum += required
        cumsum += s
    return answer

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        (smax, ss) = (X for X in sys.stdin.readline().split())

        ss = [int(s) for s in ss]

        print("Case #", case+1, ": ", solve(ss), sep="")

