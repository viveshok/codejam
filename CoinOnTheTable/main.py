#!/usr/bin/python3

import sys
#import collections

class Path:

    def __init__(self, trajectory, num_changes):
        self.trajectory = trajectory
        self.num_changes = num_changes

    def move(self, next_cell, needed_change):
        return Path(self.trajectory + [next_cell], self.num_changes + needed_change)

def solve(table, n, m, k, path):
    position = path.trajectory[-1]
    letter = table[position]
    if letter == "*":
        return path.num_changes
    elif len(path.trajectory) > k:
        return None
    else:
        i = position[0]
        j = position[1]
        solutions = list()

        # branch up
        if i > 1 and (i-1, j) not in path.trajectory:
            solutions.append(solve(table, n, m, k, path.move((i-1, j), letter != "U")))

        # branch right
        if j < m and (i, j+1) not in path.trajectory:
            solutions.append(solve(table, n, m, k, path.move((i, j+1), letter != "R")))

        # branch down
        if i < n and (i+1, j) not in path.trajectory:
            solutions.append(solve(table, n, m, k, path.move((i+1, j), letter != "D")))

        # branch left
        if j > 1 and (i, j-1) not in path.trajectory:
            solutions.append(solve(table, n, m, k, path.move((i, j-1), letter != "L")))

        try:
            return min([solution for solution in solutions if solution is not None])
        except ValueError:
            return None

if __name__ == "__main__":

    [n, m, k] = [int(X) for X in sys.stdin.readline().split()]

    table = dict()
    for i in range(1, n+1):
        for j, letter in enumerate(sys.stdin.readline().strip()):
            table[(i,j+1)] = letter

    solution = solve(table, n, m, k, Path([(1, 1)], 0))
    print(solution if solution is not None else -1)

