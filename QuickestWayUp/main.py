#!/usr/bin/python3

import sys

global transitions

def solve():
    starts = {1}
    soln = 0
    while 100 not in starts:
        starts = {j for (i, j) in transitions if i in starts}
        soln += 1

    return soln

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        sys.stdin.readline() # discard # snakes and # ladders

        ladders = [x.split(',') for x in sys.stdin.readline().split()]
        ladders = [(int(x), int(y)) for [x,y] in ladders]

        snakes = [x.split(',') for x in sys.stdin.readline().split()]
        snakes = [(int(x), int(y)) for [x,y] in snakes]

        N = 101
        transitions = {(i,j) for i in range(1, N) for j in range(i+1, i+7) if j<N}

        for (i,j) in ladders:
            transitions = {(x, y) for (x, y) in transitions if x!=i}
            transitions = {(x, y) if y!=i else (x,j) for (x, y) in transitions}
        
        for (i,j) in snakes:
            transitions = {(x, y) for (x, y) in transitions if x!=i}
            transitions = {(x, y) if y!=i else (x,j) for (x, y) in transitions}

        print(solve())

