#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
#import math
import collections

if __name__ == "__main__":

    N, M, K = [int(X) for X in sys.stdin.readline().split()]

    bikers = list()
    for biker in range(N):
        x, y = [int(X) for X in sys.stdin.readline().split()]
        bikers.append((x, y))

    bikes = list()
    for bike in range(M):
        x, y = [int(X) for X in sys.stdin.readline().split()]
        bikes.append((x, y))

    distances = list()
    for biker in bikers:
        for bike in bikes:
            delta_x = biker[0] - bike[0]
            delta_y = biker[1] - bike[1]
            distances.append((delta_x * delta_x + delta_y * delta_y, biker, bike))

    distances.sort()

    # candidate -> (bikers2bikes, bikes2bikers, i, K)
    candidates = collections.deque()
    candidates.append((dict(), dict(), 0, K))
    solution = sys.maxsize
    while candidates:
        (bikers2bikes, bikes2bikers, i, k) = candidates.popleft()
        if i >= len(distances) or distances[i-1][0]>solution:
            continue
        _distance, biker, bike = distances[i]
        if k == 0:
            solution = min(distances[i-1][0], solution)
        elif biker in bikers2bikes or bike in bikes2bikers:
            candidate = (bikers2bikes, bikes2bikers, i+1, k)
            candidates.appendleft(candidate)
            bikers2bikes = bikers2bikes.copy()
            bikes2bikers = bikes2bikers.copy()
            k -= 1
            if biker in bikers2bikes:
                old_bike = bikers2bikes[biker]
                del bikes2bikers[old_bike]
                k += 1
            if bike in bikes2bikers:
                old_biker = bikes2bikers[bike]
                del bikers2bikes[old_biker]
                k += 1
            bikers2bikes[biker] = bike
            bikes2bikers[bike] = biker
            candidate = (bikers2bikes, bikes2bikers, i+1, k)
            candidates.append(candidate)
        else:
            bikers2bikes[biker] = bike
            bikes2bikers[bike] = biker
            candidate = (bikers2bikes, bikes2bikers, i+1, k-1)
            candidates.appendleft(candidate)

    print(solution)

