#!/usr/bin/python3

import sys
#import math
#import collections

def first_method(mushrooms):
    total = 0
    for i in range(1, len(mushrooms)):
        A = mushrooms[i-1]
        B = mushrooms[i]
        total += max(0, A-B)
    return total

def second_method(mushrooms):
    max_delta = 0
    num_cases = len(mushrooms)
    for i in range(1, num_cases):
        A = mushrooms[i-1]
        B = mushrooms[i]
        max_delta = max(max_delta, A-B)

    total = 0
    for i in range(1, num_cases):
        A = mushrooms[i-1]
        B = mushrooms[i]
        total += min(max_delta, A)

    return total

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        int(sys.stdin.readline())

        mushrooms = [int(X) for X in sys.stdin.readline().split()]

        sol1 = first_method(mushrooms)
        sol2 = second_method(mushrooms)

        print("Case #", case+1, ": ", sol1, " ", sol2, sep="")

