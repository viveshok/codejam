#!/usr/bin/python3

import sys

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        K = int(sys.stdin.readline())
        x = K//2
        print(x*(x+K%2))

