#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
#import math
#import collections

def bifilter(xs, idx):
    lhs = list()
    rhs = list()
    for (i, x) in xs:
        if i < idx:
            lhs.append((i, x))
        else:
            rhs.append((i, x))
    return (lhs, rhs)

def solve(xs, ys):
    if not xs:
        return sum([y for (_i, y) in ys])
    if not ys:
        return sum([x for (_i, x) in xs])
    if xs[-1][1] >= ys[-1][1]:
        (idx, val) = xs.pop()
        (lhs, rhs) = bifilter(xs, idx)
        return val + solve(lhs, ys[:]) + solve(rhs, ys[:])
    (idx, val) = ys.pop()
    (lhs, rhs) = bifilter(ys, idx)
    return val + solve(xs[:], lhs) + solve(xs[:], rhs)

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        sys.stdin.readline() # skip M & N

        ys = [(i, int(y)) for (i, y) in enumerate(sys.stdin.readline().split())]
        xs = [(i, int(x)) for (i, x) in enumerate(sys.stdin.readline().split())]

        ans = solve(sorted(xs, key=lambda X: X[1]), sorted(ys, key=lambda Y: Y[1]))
        print(ans % 1000000007)

