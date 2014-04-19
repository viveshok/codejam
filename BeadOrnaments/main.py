#!/usr/bin/python3

import sys

class Bead:
    def __init__(self, color):
        self.color = color
        self.bead = None

def solve(beads, Ornament):
    if beads:
        if Ornament:
            # return ...
        else:
            # return solve()...
    else:
        return 1

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        N = int(sys.stdin.readline())

        beads = [int(X) for X in sys.stdin.readline().split()]

        print(solve(beads, None))

