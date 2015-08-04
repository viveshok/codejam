#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
#import math
#import collections

def solve(listA, listB):
    if not listA and not listB:
        return True
    if not listB and listA[0] == 0:
        return False
    if listA[0] == 1 and solve(listB, listA[1:]):
        return True
    if listA[0] == listB[0] and solve(listA[1:], listB[1:]):
        return True
    if len(listA) > 1 and listA[0] == listA[1]:
        if len(listB) > 1 and listB[0] == listB[1] and solve(listA[2:], listB[2:]):
            return True
        if listB[0] == 1:
            return solve(listB[1:], listA[2:])

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for _case in range(T):

        _N = sys.stdin.readline()

        listA = [int(X) for X in sys.stdin.readline().strip()]

        listB = [int(X) for X in sys.stdin.readline().strip()]

        print("YES" if solve(listA, listB) else "NO")

