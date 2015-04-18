#!/usr/bin/python3

import sys
#import math
import collections

def minutes(N, Ms):
    minutes_ = collections.defaultdict(int)
    minutes_[0] = len(Ms)
    for i in range(1, N*10000):
        for M,freq in Ms.items():
            if M%i==0:
                minutes_[i] += freq

#    upper_bound = min(N*min(Ms), 10000000000)
#    for M,freq in Ms.items():
#        for i in range(0, upper_bound, M):
#            minutes_[i] += freq

    return minutes_

def minute(N, minutes_):
    i = 0
    while N > 0:
        if minutes_[i] >= N:
            break
        else:
            N -= minutes_[i]
            i += 1

    return (i, N)


if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        [_, N] = [int(X) for X in sys.stdin.readline().split()]

        Ms = [int(X) for X in sys.stdin.readline().split()]

        minutes_ = minutes(N, collections.Counter(Ms))

        minute_, rank = minute(N, minutes_)

        for i, M in enumerate(Ms):
            if minute_%M == 0 and rank == 1:
                print("Case #", case+1, ": ", i+1, sep="")
                break
            if minute_%M == 0:
                rank -= 1

