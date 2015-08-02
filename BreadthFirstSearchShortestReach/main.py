#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
#import math
#import collections

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        [N, M] = [int(X) for X in sys.stdin.readline().split()]

        # build adjacency list for graph
        G = [set() for n in range(N)]

        for m in range(M):
            [s, t] = [int(X)-1 for X in sys.stdin.readline().split()]
            G[s].add(t)
            G[t].add(s)

        S = int(sys.stdin.readline()) - 1

        distances = [-1 for n in range(N)]
        visiting = [(S, 0)]
        visited = {S}
        while visiting:
            current, distance = visiting[0]
            visiting.pop(0)
            distances[current] = distance
            nexts = G[current] - visited
            visited |= nexts
            visiting.extend([(next_, distance+6) for next_ in nexts])

        distances.pop(S)
        for distance in distances:
            print(distance, end=' ')
        print()

