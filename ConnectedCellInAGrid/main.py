#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
#import math
import collections

if __name__ == "__main__":

    m = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    matrix = [[] for x in range(m)]
    roots = [[] for x in range(m)]

    def root(i, j):
        if roots[i][j]:
            (m, n) = roots[i][j]
            if (m, n) == (i, j):
                return (i, j)
            else:
                (m, n) = root(m, n)
                roots[i][j] = (m, n)
                return (m, n)
        return none

    def print_roots():
        for row in roots:
            for root in row:
                print(" {} ".format(root), end="")
            print()

    for i in range(m):
        row = [int(X) for X in sys.stdin.readline().split()]
        for (j, x) in enumerate(row):
            matrix[i].append(x)
            root_ = None
            if x:
                if j>0 and matrix[i][j-1]:
                    root_ = root(i, j-1)
                if j>0 and i>0 and matrix[i-1][j-1]:
                    if root_:
                        (a, b) = root(i-1, j-1)
                        roots[a][b] = root_
                    else:
                        root_ = root(i-1, j-1)
                if i>0 and matrix[i-1][j]:
                    if root_:
                        (a, b) = root(i-1, j)
                        roots[a][b] = root_
                    else:
                        root_ = root(i-1, j)
                if j<n-1 and i>0 and matrix[i-1][j+1]:
                    if root_:
                        (a, b) = root(i-1, j+1)
                        roots[a][b] = root_
                    else:
                        root_ = root(i-1, j+1)
                root_ = root_ if root_ else (i, j)

            roots[i].append(root_)

    counts = collections.defaultdict(int)
    for row in roots:
        for (i,j) in [root_ for root_ in row if root_]:
            (m, n) = root(i, j)
            counts[(m, n)] += 1

    #print_roots()

    print(max(counts.values()))

