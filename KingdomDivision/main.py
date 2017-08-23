
# how to
# $ python3 -m doctest -v main.py # to test
# $ python3 main.py < input > output # to run

import sys
#import math
import collections

if __name__ == "__main__":

    _ = int(sys.stdin.readline())

    roads = collections.defaultdict(list)

    for line in sys.stdin:

        [N, C] = [int(X) for X in line.split()]

        roads[N].append(C)
        roads[C].append(N)

    print(dict(roads))

#    solution = 2 * (1 + solve(list(roads.keys())[0], roads, set()))
#    print(solution)
#    mod = 10 ** 9 + 7
#    print(solution % mod)

