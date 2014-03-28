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
    numbers = [(i, True) for i in range(2, N+1)]
    p = 2
    counter = p+p
    while p < N:
        while counter <= N:
            numbers[counter-2] = (counter, False)
            counter += p
        
        p = next((i for i, v in numbers[p:] if v), N) 
        counter = p+p

    return [i for i, v in numbers if v]


if __name__ == "__main__":

    ## find number of ways to build wall, memoize
    #num_ways_ = dict()
    #for i in range(1, 41):
    #    num_ways_[i] = num_ways(i, [1, 4])
    #print("num_ways_ =", num_ways_)

    ## find all primes up to num_ways_[40],
    ## using sieve of eratosthenes
    #primes = sieve(num_ways_[40])

    ## compute answer for all possible N = 1, ..., 40, memoize
    #num_primes = dict()
    #for i, v in num_ways_.items():
    #    num_primes[i] = len([x for x in primes if x <= v])

    num_primes = {1: 0, 2: 0, 3: 0, 4: 1, 5: 2, 6: 2, 7: 3, 8: 4, 9: 5, 10: 7, 11: 9, 12: 10, 13: 12, 14: 16, 15: 20, 16: 25, 17: 33, 18: 43, 19: 54, 20: 69, 21: 92, 22: 120, 23: 156, 24: 205, 25: 270, 26: 355, 27: 463, 28: 616, 29: 817, 30: 1078, 31: 1433, 32: 1913, 33: 2544, 34: 3386, 35: 4523, 36: 6049, 37: 8079, 38: 10795, 39: 14476, 40: 19386}

    T = int(sys.stdin.readline())

    for case in range(T):

        N = int(sys.stdin.readline())

        print(num_primes[N])

