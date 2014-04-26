#!/usr/bin/python3

import sys

if __name__ == "__main__":

    N = int(sys.stdin.readline())

    numbers = sorted([int(X) for X in sys.stdin.readline().split()])

    for i in range(0, N, 2):
        if i == N-1 or numbers[i] != numbers[i+1]:
            print(numbers[i])
            break

