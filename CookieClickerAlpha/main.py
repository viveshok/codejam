#!/usr/bin/python3

import sys

def solve(C, F, X, rate, time):

#    if C/rate+X/(rate+F) >= X/rate:
#        return time+X/rate
#
#    return solve(C, F, X, rate+F, time+C/rate)


    while C/rate+X/(rate+F) < X/rate:
        rate += F
        time += C/rate

    return time+X/rate


if __name__ == "__main__":

    sys.setrecursionlimit(18500)

    T = int(sys.stdin.readline())

    for case in range(T):

        [C, F, X] = [float(X) for X in sys.stdin.readline().split()]

        Ans = solve(C, F, X, 2.00, 0.0)

        print("Case #", case+1, ": ", Ans, sep="")

