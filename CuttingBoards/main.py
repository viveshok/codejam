#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
#import math
#import collections

def solve(xs, ys):
    ans = 0
    while xs or ys:
        if not xs:
            return ans + sum([y for (_i, y) in ys])
        if not ys:
            return ans + sum([x for (_i, x) in xs])
        if xs[-1][1] >= ys[-1][1]:
            (idx, val) = xs.pop()
            ans += val + sum([y for (_i, y) in ys])
        else:
            (idx, val) = ys.pop()
            ans += val + sum([x for (_i, x) in xs])

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        sys.stdin.readline() # skip M & N

        ys = [(i, int(y)) for (i, y) in enumerate(sys.stdin.readline().split())]
        xs = [(i, int(x)) for (i, x) in enumerate(sys.stdin.readline().split())]

        ans = solve(sorted(xs, key=lambda X: X[1]), sorted(ys, key=lambda Y: Y[1]))
        print(ans % 1000000007)

