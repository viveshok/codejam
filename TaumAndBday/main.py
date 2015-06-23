#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
#import math
#import collections

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        [B, W] = [int(X) for X in sys.stdin.readline().split()]
        [X, Y, Z] = [int(X) for X in sys.stdin.readline().split()]

        cost_black = min(X, Y+Z)
        cost_white = min(Y, X+Z)

        print(B*cost_black+W*cost_white)

