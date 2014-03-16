#!/usr/bin/python3

import sys

if __name__ == "__main__":

    [r, c] = [int(X) for X in sys.stdin.readline().split()]

    suitable = []
    for i in range(r):
        for j, char in enumerate(sys.stdin.readline().split()):
            if char == '1':
                suitable.append((i,j))

    print(suitable)

