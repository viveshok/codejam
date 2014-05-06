#!/usr/bin/python3

import sys
import collections

def dist(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

if __name__ == "__main__":

    [n, m, k] = [int(X) for X in sys.stdin.readline().split()]

    table = dict()
    for i in range(1, n+1):
        for j, letter in enumerate(sys.stdin.readline().strip()):
            if letter == "*":
                goal = (i, j+1)
            table[(i,j+1)] = letter

    cache = collections.defaultdict(lambda: 105)

    def dist(p):
        return abs(p[0]-goal[0]) + abs(p[1]-goal[1])

    def solve(position, t, num_changes):
        cache[position] = num_changes
        letter = table[position]
        if position == goal:
            return num_changes
        else:
            i = position[0]
            j = position[1]
            solutions = list()

            # branch up
            if i > 1 and cache[(i-1, j)] > num_changes + (letter != "U") and dist((i-1, j)) < k-t:
                solutions.append(solve((i-1, j), t+1, num_changes + (letter != "U")))

            # branch right
            if j < m and cache[(i, j+1)] > num_changes + (letter != "R") and dist((i, j+1)) < k-t:
                solutions.append(solve((i, j+1), t+1, num_changes + (letter != "R")))

            # branch down
            if i < n and cache[(i+1, j)] > num_changes + (letter != "D") and dist((i+1, j)) < k-t:
                solutions.append(solve((i+1, j), t+1, num_changes + (letter != "D")))

            # branch left
            if j > 1 and cache[(i, j-1)] > num_changes + (letter != "L") and dist((i, j-1)) < k-t:
                solutions.append(solve((i, j-1), t+1, num_changes + (letter != "L")))

            try:
                return min([solution for solution in solutions if solution is not None])
            except ValueError:
                return None


    solution = solve((1, 1), 0, 0)
    print(solution if solution is not None else -1)

