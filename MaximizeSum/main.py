#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
import bisect

def solve(xs, M):

    xs = [0] + xs

    cumsum = xs[0]
    cumsums = [cumsum]
    maximum = -sys.maxsize

    for x in xs[1:]:
        cumsum = (cumsum + x) % M
        candidate_index = bisect.bisect(cumsums, (cumsum-M) % M)

        if candidate_index < len(cumsums):
            maximum = max(maximum, (cumsum-cumsums[candidate_index]) % M)
        else:
            maximum = max(maximum, cumsum)

        bisect.insort(cumsums, cumsum)

    return maximum

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        [N_, M] = [int(X) for X in sys.stdin.readline().split()]

        xs = [int(X) for X in sys.stdin.readline().split()]

        print(solve(xs, M))

