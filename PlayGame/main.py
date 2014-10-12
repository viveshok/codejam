#!/usr/bin/python3

import sys
#import math
#import collections

def add_score(scores, player, increment):
    (player0, player1) = scores
    if player == 0:
        return (player0+increment, player1)
    else:
        return (player0, player1+increment)

def solve(bricks, scores, turn):

    if len(bricks) <= 3:
        remaining = sum(bricks)
        return add_score(scores, turn, remaining)

    scenarii = [0, 0, 0]
    for i in range(3):
        inc = sum(bricks[:i+1])
        scenarii[i] = solve(bricks[i+1:], add_score(scores,turn,inc), 1-turn)

    return max(scenarii, key=lambda x: x[turn])

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        sys.stdin.readline()
        bricks = [int(X) for X in sys.stdin.readline().split()]

        scores = solve(bricks, (0, 0), 0)
        print(scores[0])

