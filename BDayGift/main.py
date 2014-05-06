#!/usr/bin/python3

import sys
#import collections

if __name__ == "__main__":

    N = int(sys.stdin.readline())

    the_sum = 0
    for ball in range(N):
        the_sum += int(sys.stdin.readline())

    print(the_sum/2)

