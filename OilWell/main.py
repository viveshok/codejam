#!/usr/bin/python3

import sys

class Border(object):

    def __init__(self, points):
        [self.x0, self.y0, self.x1, self.y1] = [None, None, None, None]
        for (i, j) in points:
            self.x0 = min(i, self.x0) if self.x0 is not None else i
            self.y0 = min(j, self.y0) if self.y0 is not None else j
            self.x1 = max(i, self.x1) if self.x1 is not None else i
            self.y1 = max(j, self.y1) if self.y1 is not None else j

    def on_border(self, point):
        return point[0]==self.x0 or point[0]==self.x1 or point[1]==self.y0 or point[1]==self.y1

    def max_dist(self, point):
        return max(abs(self.x0-point[0]), abs(self.x1-point[0]), abs(self.y0-point[1]), abs(self.y1-point[1]))

def solve(points, border):
    if len(points) > 1:
        candidates = []
        for point in points:
            if border.on_border(point):
                points_ = points-{point}
                border_ = Border(points_)
                candidates.append(border_.max_dist(point) + solve(points_, border_))
        return min(candidates)
    else:
        return 0

if __name__ == "__main__":

    [r, _] = [int(X) for X in sys.stdin.readline().split()]

    points = set()

    for i in range(r):
        for j, char in enumerate(sys.stdin.readline().split()):
            if char == '1':
                points.add((i, j))

    print(solve(points, Border(points)))

