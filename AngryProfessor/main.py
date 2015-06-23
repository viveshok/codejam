#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
#import math
#import collections

def solve(students, K):
    count = 0
    for student in students:
        if student <= 0:
            count += 1
        if count >= K:
            return "NO"
    return "YES"

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        [_, K] = [int(X) for X in sys.stdin.readline().split()]

        students = [int(X) for X in sys.stdin.readline().split()]

        print(solve(students, K))

