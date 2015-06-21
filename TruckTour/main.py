#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
#import math
#import collections

if __name__ == "__main__":

    N = int(sys.stdin.readline())

    stations = []
    for station in range(N):
        stations.append(tuple([int(X) for X in sys.stdin.readline().split()]))

    tank = 0
    start = 0
    position = 0
    for petrol, distance in stations:
#        fmt = "start: {:d} position: {:d} tank: {:d} petrol: {:d} distance: {:d}"
#        print(fmt.format(start, position, tank, petrol, distance))
        position += 1
        if tank + petrol < distance:
            start = position
            tank = 0
        else:
            tank += petrol-distance

    print(start)

