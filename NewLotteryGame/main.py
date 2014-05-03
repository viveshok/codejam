#!/usr/bin/python3

import sys
#import collections

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        [A, B, K] = [int(X) for X in sys.stdin.readline().split()]

        count = 0
        for a in range(K, A):
            for b in range(K, B):
                if a&b<K:
                    count += 1

        print("Case #", case+1, ": ", (A-K)*K+(B-K)*K+(K*K)+count, sep="")

