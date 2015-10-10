
# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
from scipy import optimize
#import math
#import collections

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

    c = list()
    A_ub = list()
    for i, bike in enumerate(bikes):
        A_ub.append(i*M*[0]+M*[1]+(M-i-1)*M*[0])
        for biker in bikers:
            delta_x = biker[0] - bike[0]
            delta_y = biker[1] - bike[1]
            c.append(abs(delta_x) + abs(delta_y))

    b_ub = [1]*M
    A_eq = [[1]*N*M]
    b_eq = [K]
    bounds = [(0, 1) for i in range(M*N)]

    result = optimize.linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds)
    distances = [C*X for C,X in zip(c, result.x)]
    max_dist = max(distances)
    print(int(max_dist*max_dist))

