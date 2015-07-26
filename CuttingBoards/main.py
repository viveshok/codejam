#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
#import math
#import collections

def cum_sum(xs):
    sum_ = 0
    result = list()
    for x in xs:
        sum_ += x
        result.append(sum_)
    return result

def solve(xs, ys):
    cum_xs = cum_sum(xs)
    cum_ys = cum_sum(ys)
    ans = 0
    while xs or ys:
        if not xs:
            return ans + cum_ys.pop()
        if not ys:
            return ans + cum_xs.pop()
        if xs[-1] >= ys[-1]:
            cum_xs.pop()
            ans += xs.pop() + cum_ys[-1]
        else:
            cum_ys.pop()
            ans += ys.pop() + cum_xs[-1]

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        sys.stdin.readline() # skip M & N

        ys = sorted([int(y) for y in sys.stdin.readline().split()])
        xs = sorted([int(x) for x in sys.stdin.readline().split()])

        ans = solve(xs, ys)
        print(ans % 1000000007)

