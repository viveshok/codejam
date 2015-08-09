#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
#import math
#import collections

INT = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}

def mod(x):
    return x % 1000000007

def solve(S):
    answer = INT[S.__next__()]
    prefix_sum = answer
    x = 11
    for char in S:
        prefix_sum = INT[char] * x + prefix_sum
        answer += prefix_sum
        x = 10 * mod(x) + 1
    return answer

if __name__ == "__main__":
    S = sys.stdin.readline().strip()
    print(mod(solve(reversed(S))))

