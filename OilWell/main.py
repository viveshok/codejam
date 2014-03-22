#!/usr/bin/python3

import sys
import collections

def acme_distance(a, b):
    return max(abs(b[0]-a[0]), abs(b[1]-a[1]))

def cull(vertices, p):
    result = dict()
    for k, vs in vertices.items():
        non_overlapping = [v for v in vs if p not in v]
        if non_overlapping:
            result[k] = non_overlapping
    return result

def solve(vertices, acc):
    if vertices:
        solns = []
        dist = max(vertices.keys())
        for (p0, p1) in vertices[dist]:
            solns.append(solve(cull(vertices, p0), acc+dist))
            solns.append(solve(cull(vertices, p1), acc+dist))
        return min(solns)
    else:
        return acc

def get_vertices(points):
    vertices = collections.defaultdict(list)
    while points:
        p0 = points.pop()
        for p in points:
            vertices[acme_distance(p0, p)].append({p0, p})

    return vertices

if __name__ == "__main__":

    [r, c] = [int(X) for X in sys.stdin.readline().split()]

    points = set()
    for i in range(r):
        for j, char in enumerate(sys.stdin.readline().split()):
            if char == '1':
                points.add((i,j))

    print(solve(get_vertices(points), 0))

