#!/usr/bin/python3

import sys

def cull_xs(xs, x

def solve(xs, ys, acc):
    if xs:
        max_dist_x = xs[-1] - xs[0]
        max_dist_y = ys[-1] - ys[0]
        if max_dist_x >= max_dist_y:
            left = solve(xs[:-1], cull(ys, xs[-1]), acc+max_dist_x)
            right = solve(xs[1:], cull(ys, xs[0]), acc+max_dist_x)
            return min(left, right)
        else:
            left = solve(cull_xs(xs, ys[-1]), ys[:-1], acc+max_dist_x)
            right = solve(cull(xs, ys[0]), ys[1:], acc+max_dist_x)
            return min(left, right)
    else:
        return acc

if __name__ == "__main__":

    [r, c] = [int(X) for X in sys.stdin.readline().split()]

    xs = []
    ys = []
    locations_xs = {}
    locations_ys = {}

    for i in range(r):
        for j, char in enumerate(sys.stdin.readline().split()):
            if char == '1':
                xs.append(i)
                ys.append(j)
                location_xs(j) = i
                location_ys(i) = j
                POINTS.append((i,j))

    print(solve(xs, sorted(ys), locations_xs, locations_ys, 0))

