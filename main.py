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

        [N, C] = [int(X) for X in sys.stdin.readline().split()]

        Ans = N + C

        print("Case #", case+1, ": ", Ans, sep="")

