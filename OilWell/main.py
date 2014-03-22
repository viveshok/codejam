#!/usr/bin/python3

import sys
import collections

def acme_distance(a, b):
    return max(abs(b[0]-a[0]), abs(b[1]-a[1]))

def get_vertices(points):
    vertices = collections.defaultdict(list)
    while points:
        p0 = points.pop()
        for p1 in points:
            vertices[acme_distance(p0, p1)].append((p0, p1))

    return vertices

if __name__ == "__main__":

    [r, c] = [int(X) for X in sys.stdin.readline().split()]

    points = []

    for i in range(r):
        for j, char in enumerate(sys.stdin.readline().split()):
            if char == '1':
                points.append((i, j))

    tmp = 0
    for k, v in get_vertices(points).items():
        print("k:",k,", len(v):", len(v))
        tmp += len(v)

    print("tmp: ", tmp)

