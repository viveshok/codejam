#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
#import math
#import collections

# tree := set of ints
# forest := array -> index is node-1, value is tree id

class Edge():
    def __init__(self, node_one, node_two, weight):
        self.n1 = node_one
        self.n2 = node_two
        self.w = weight
    def __lt__(self, other):
        return self.w < other.w
    def __repr__(self):
        return "node A: {} weight: {} node B: {}".format(self.n1, self.w, self.n2)

if __name__ == "__main__":

    [N, M] = [int(X) for X in sys.stdin.readline().split()]

    edges = list()
    for _edge in range(M):
        [x, y, r] = [int(X) for X in sys.stdin.readline().split()]
        edges.append(Edge(x-1, y-1, r))
    forest = list(range(N))

    _S = int(sys.stdin.readline())

    edges.sort(reverse=True)

    result = 0

    while edges:
        e = edges.pop()
        if forest[e.n1] != forest[e.n2]:
            old, new = sorted([forest[e.n1], forest[e.n2]])
            forest = [new if x==old else x for x in forest]
            result += e.w

    print(result)

