#!/usr/bin/python3

import sys

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    numbers = sorted([int(X) for X in sys.stdin.readline().split()])

    # biggest than maximum distance as specified in constraints
    closest_distance = 20000001
    solutions = list()
    for i, left in enumerate(numbers[:-1]):
        right = numbers[i+1]
        if right-left < closest_distance:
            solutions = [(left, right)]
            closest_distance = right-left
        elif right-left == closest_distance:
            solutions.append((left, right))

    for (left, right) in solutions:
        print(left, right, end=" ")

