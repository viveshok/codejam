#!/usr/bin/python3

import sys
import collections

def solve(tree, parent, node, removals):
    if len(tree[node]) == 1:
        return 0


    nexts = tree[node] - parent

    if len(tree[node]) == 2:
        return 1+min(solve(tree, tree[node], # ..........


def remove_edge(tree, a, b):
    for k in tree:
        if (k==a and b in tree[k]):
            tree[k].remove(b)
        if (k==b and a in tree[k]):
            tree[k].remove(a)

    return tree

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    sys.stdin.readline()

    for case in range(T):

        tree = collections.defaultdict(set)

        while True:
            try:
                [h, t] = [int(X) for X in sys.stdin.readline().split()]
                tree[h].add(t)
                tree[t].add(h)
            except ValueError:
                break

        for k in tree:
            print(k, tree[k])


        candidates = [k for k,v in tree.items() if len(v) in (2,3)]

        for c in candidates:


