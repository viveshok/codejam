#!/usr/bin/python3

import sys

def solve(num_fives, num_threes):
    if num_fives%3==0:
        return (True, num_fives, num_threes)
    elif num_fives < 5:
        return (False, 0, 0)
    else:
        return solve(num_fives-5, num_threes+5)

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        N = int(sys.stdin.readline())

        (possible, num_fives, num_threes) = solve(N, 0)

        print(-1) if not possible else print(num_fives*'5'+num_threes*'3')

