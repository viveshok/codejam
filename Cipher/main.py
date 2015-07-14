#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
#import math
#import collections

if __name__ == "__main__":

    [N, K] = [int(X) for X in sys.stdin.readline().split()]

    if K==1:
        print(sys.stdin.readline())
        sys.exit(0)

    K = min(K, N)

    S = [int(X) for X in sys.stdin.readline().strip()]

    acc = S[0]
    results = [acc]

    for i in range(1, K):
        result = acc ^ S[i]
        acc ^= result
        results.append(result)

    acc = 0
    for x in results[1:K]:
        acc ^= x

    for i in range(K, N):
        result = acc^S[i]
        results.append(result)
        acc = results[i-K+1] ^ acc ^ result

    print("".join([str(result) for result in results]))

