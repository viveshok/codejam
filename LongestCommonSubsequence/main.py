#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
#import math
#import collections

def print_matrix(M):
    for row in M:
        for item in row:
            print(item, end=' ')
        print()

if __name__ == "__main__":

    [n, m] = [int(X) for X in sys.stdin.readline().split()]

    As = sys.stdin.readline().split()
    Bs = sys.stdin.readline().split()

    C = [[0] for i in range(n+1)]
    C[0] = [0 for j in range(m+1)]
    for i, a in enumerate(As):
        for j, b in enumerate(Bs):
            C[i+1].append(C[i][j] + 1 if a == b else max(C[i][j+1], C[i+1][j]))

    result = []
    while m and n:
        if As[n-1] == Bs[m-1]:
            result.append(As[n-1])
            m, n = m-1, n-1
        else:
            n, m = (n, m-1) if C[n][m-1] >= C[n-1][m] else (n-1, m)

    print(' '.join(reversed(result)))

