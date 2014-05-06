#!/usr/bin/python3

import sys
#import collections

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        [Px, Py, Qx, Qy] = [int(X) for X in sys.stdin.readline().split()]

        print(Qx-(Px-Qx), Qy-(Py-Qy))

