#!/usr/bin/python3

import sys

def num_ways(N, values):

    if N==0:
        return 1
    if N < 0:
        return 0

    result = 0
    for (i, v) in enumerate(values):
        result += num_ways(N-v, values)

    return result

def sieve(N):
    ledger = [True] * (N+1) 
    ledger[0] = False # 0 is not prime
    ledger[1] = False # 1 is not prime

    primes = []
    while True:
        try:
            next_prime = next(i for i, v in enumerate(ledger) if v)
            primes.append(next_prime)
            for i in range(next_prime, N+1, next_prime):
                ledger[i] = False
        except StopIteration:
            break

    return primes

if __name__ == "__main__":

#    # find number of ways to build wall, memoize
#    num_ways_ = dict()
#    for i in range(1, 41):
#        num_ways_[i] = num_ways(i, [1, 4])
#
#    # find all primes up to num_ways_[40],
#    # using sieve of eratosthenes
#    primes = sieve(num_ways_[40])
#
#    # compute answer for all possible N = 1, ..., 40, memoize
#    num_primes = dict()
#    for i, v in num_ways_.items():
#        num_primes[i] = len([x for x in primes if x <= v])
#    print("num_primes =", num_primes)

    num_primes = {1: 0, 2: 0, 3: 0, 4: 1, 5: 2, 6: 2, 7: 3, 8: 4, 9: 4, 10: 6, 11: 8, 12: 9, 13: 11, 14: 15, 15: 19, 16: 24, 17: 32, 18: 42, 19: 53, 20: 68, 21: 91, 22: 119, 23: 155, 24: 204, 25: 269, 26: 354, 27: 462, 28: 615, 29: 816, 30: 1077, 31: 1432, 32: 1912, 33: 2543, 34: 3385, 35: 4522, 36: 6048, 37: 8078, 38: 10794, 39: 14475, 40: 19385}

    T = int(sys.stdin.readline())

    for case in range(T):

        N = int(sys.stdin.readline())

        print(num_primes[N])

