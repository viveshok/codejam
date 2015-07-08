#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
#import math
#import collections

if __name__ == "__main__":

    [M, N, R] = [int(X) for X in sys.stdin.readline().split()]

    NUM_LAYERS = min(M, N)//2

    matrix = list()
    for i in range(M):
        matrix.append(sys.stdin.readline().split())

    layers = []
    for i in range(NUM_LAYERS):

        # shave top
        layer = matrix.pop(0)

        # shave right side
        layer.extend([row.pop() for row in matrix])

        # shave bottom
        layer.extend(reversed(matrix.pop()))

        # shave left side
        layer.extend(reversed([row.pop(0) for row in matrix]))

        # rotate layer
        r = R % len(layer)
        layers.append(layer[r:]+layer[:r])

    layers.reverse()

    # build core
    if M>N:
        matrix = [layers[0][:2]]
        remainder = layers[0][2:]
        while remainder:
            matrix.append([remainder.pop(), remainder.pop(0)])
    else:
        matrix = [layers[0][:len(layers[0])//2],
                  list(reversed(layers[0][len(layers[0])//2:]))]

    for layer in layers[1:]:

        m = len(matrix)+2
        n = len(matrix[0])+2

        # attach top
        matrix.insert(0, layer[:n])

        # attach right side
        for i, x in enumerate(layer[n:n+m-2]):
            matrix[i+1].append(x)

        # attach bottom
        matrix.append(list(reversed(layer[n+m-2:2*n+m-2])))

        # attach left side
        for i, x in enumerate(reversed(layer[2*n+m-2:])):
            matrix[i+1].insert(0, x)

    for i in range(M):
        for j in range(N):
            print(matrix[i][j], end=' ')
        print()

