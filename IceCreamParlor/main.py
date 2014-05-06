#!/usr/bin/python3

import sys
#import collections

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        M = int(sys.stdin.readline())
        N = int(sys.stdin.readline())
        cis = [int(X) for X in sys.stdin.readline().split()]

        match = dict()
        for i, ci in enumerate(cis):
            if ci in match:
                print(match[ci]+1, i+1)
                break
            match[M-ci] = i

