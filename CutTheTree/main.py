#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
#import math
#import collections

if  __name__ == "__main__":

    N = int(sys.stdin.readline())

    vertices_weights = [int(X) for X in sys.stdin.readline().split()]
    subtrees_weights = vertices_weights[:]


    G = {i:set() for i in range(N)}

    for edge in range(N-1):
        [v1, v2] = [int(X)-1 for X in sys.stdin.readline().split()]
        G[v1].add(v2)
        G[v2].add(v1)

    for vertex in G:
        if len(G[vertex]) <= 2:
            root = vertex # pick arbitrary root
            break

    # first DFS - find weigth of each subtree
    visited = set()
    visiting = [root]
    while visiting:
        parent = visiting[-1]
        visited.add(parent)
        childs = G[parent] - visited
        if childs:
            for child in childs:
                G[child].remove(parent)
                visiting.append(child)
        else:
            parent = visiting.pop()
            subtrees_weights[parent] += sum([subtrees_weights[i] for i in G[parent]])

    # second DFS - find minimum difference
    min_diff = sys.maxsize
    visited = set()
    visiting = [(root, 0)] # vertex, path_weight
    while visiting:
        parent, path_weight = visiting[-1]
        visited.add(parent)
        childs = G[parent] - visited
        if childs:
            for child in childs:
                lhs = path_weight + vertices_weights[parent] + sum([subtrees_weights[i] for i in childs - {child}])
                rhs = subtrees_weights[child]
                min_diff = min(min_diff, abs(lhs - rhs))
                visiting.append((child, lhs))
        else:
            _parent, _path_weight = visiting.pop()

    print(min_diff)

