#!/usr/bin/python3

import sys
#import collections

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        N = int(sys.stdin.readline())

        if N%2==1:
            print(2)
        elif N%4==0:
            print(3)
        else:
            print(4)

