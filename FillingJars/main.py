#!/usr/bin/python3

import sys
import functools

if __name__ == "__main__":

    [N, M] = [int(X) for X in sys.stdin.readline().split()]

    operations = [tuple(sys.stdin.readline().split()) for X in range(M)]

    f = lambda acc, op: acc+((int(op[1])-int(op[0])+1)*int(op[2]))
    avg = functools.reduce(f, operations, 0) // N

    print(avg)

