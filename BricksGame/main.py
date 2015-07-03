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

        N = int(sys.stdin.readline())

        bs = [int(X) for X in sys.stdin.readline().split()]

        bs.reverse()

        scores = [(sum(bs[:i]), 0) for i in [1, 2, 3]]

        for i in range(3, N):
            score_take_1 = (bs[i] + scores[i-1][1], scores[i-1][0])
            score_take_2 = (bs[i] + bs[i-1] + scores[i-2][1], scores[i-2][0])
            score_take_3 = (bs[i] + bs[i-1] + bs[i-2] + scores[i-3][1], scores[i-3][0])
            scores.append(max(score_take_1, score_take_2, score_take_3))

        print(scores[-1][0])

