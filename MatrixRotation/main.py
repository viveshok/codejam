#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
import math
#import collections

def memoize(function):
    cache = dict()
    def memoized_function(*args):
        if args in cache:
            return cache[args]
        else:
            result = function(*args)
            cache[args] = result
            return result
    return memoized_function

if __name__ == "__main__":

    [M, N, R] = [int(X) for X in sys.stdin.readline().split()]

    NUM_LAYERS = min(M, N)/2
    THICKNESS_CORE_X = N/2 - NUM_LAYERS + 1
    THICKNESS_CORE_Y = M/2 - NUM_LAYERS + 1

    def layer(i, j, M, N):
        '''
        >>> layer(0, 0, 4, 5)
        2
        >>> layer(0, 2, 4, 5)
        2
        >>> layer(1, 1, 4, 5)
        1
        >>> layer(1, 2, 4, 5)
        1
        >>> layer(0, 3, 4, 5)
        2
        >>> layer(1, 3, 4, 5)
        1
        >>> layer(0, 0, 2, 6)
        1
        '''

        distance_x = N/2-j if j<N/2 else j-N/2+1
        layer_x = max(distance_x-THICKNESS_CORE_X+1, 1)

        distance_y = M/2-i if i<M/2 else i-M/2+1
        layer_y = max(distance_y-THICKNESS_CORE_Y+1, 1)

        return round(max(layer_x, layer_y))

    @memoize
    def range_(M, N, L):
        return 2 * L + (N-M if M<N else 0)

    def shift(i, j, M, N, R):
        L = layer(i, j, M, N)
        r_x = range_(M, N, L)
        r_y = range_(N, M, L)
        R %= 2*r_x + 2*r_y - 4
        while R > 0:
            if M//2-i == L and j<N//2+L-1: # shift right
                delta = min(math.ceil(N/2)+L-j-1, R)
                j += delta
                R -= delta
            elif j-math.ceil(N/2)+1 == L and i<math.ceil(M/2)+L-1: # shift down
                delta = min(math.ceil(M/2)+L-i-1, R)
                i += delta
                R -= delta
            elif i-math.ceil(M/2)+1 == L and j>=N//2-L+1: # shift left
                delta = min(j-N//2+L, R)
                j -= delta
                R -= delta
            elif N//2-j == L and i>=M//2-L+1: # shift up
                delta = min(i-M//2+L, R)
                i -= delta
                R -= delta
        return (i, j)

    matrix = list()
    for i in range(M):
        matrix.append(sys.stdin.readline().split())

    for i in range(M):
        for j in range(N):
            (old_i, old_j) = shift(i, j, M, N, R)
            print("{} ".format(matrix[old_i][old_j]), end="")
        print()

