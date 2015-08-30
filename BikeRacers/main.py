#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
import numpy
#import math
#import collections

# hungarian algorithm for perfect matching of bipartite graph

def lines(matrix, axes):
    lines_ = list()
    zeros = matrix == 0
    while numpy.any(zeros):
        axis, index, line_ = axes.pop()
        if axis == 0:
            zeros[index] = False
        if axis == 1:
            zeros[:, index] = False
        lines_.append((axis, index))
    return lines_

def all_axes(matrix, N, M):
    axes = []
    for i in range(N):
        axes.append((0, i, matrix[i]))
    for j in range(M):
        axes.append((1, j, matrix[:,j]))
    axes.sort(key=lambda axis: sum([x==0 for x in axis[2]]))
    return axes

if __name__ == "__main__":

    N, M, K = [int(X) for X in sys.stdin.readline().split()]

    bikers = list()
    for biker in range(N):
        x, y = [int(X) for X in sys.stdin.readline().split()]
        bikers.append((x, y))

    bikes = list()
    for bike in range(M):
        x, y = [int(X) for X in sys.stdin.readline().split()]
        bikes.append((x, y))

    cost_matrix = numpy.zeros((N, M))
    for i, biker in enumerate(bikers):
        for j, bike in enumerate(bikes):
            delta_x = biker[0] - bike[0]
            delta_y = biker[1] - bike[1]
            cost_matrix[i, j] = delta_x * delta_x + delta_y * delta_y

    # step 1
    aux = cost_matrix - cost_matrix.min(1).reshape(N, 1)

    # step 2
    aux -= aux.min(0)

    # step 3
    axes = all_axes(aux, N, M)
    lines_ = lines(aux, axes)

    # step 4

    print(lines_)

