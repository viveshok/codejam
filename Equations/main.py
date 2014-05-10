#!/usr/bin/python3

import sys
import math
import collections

'''
Somes notes on a way to reach solution:

    1/x + 1/y = 1/N!
         vvv
    x N! + y N! = xy
         vvv
    0 = xy - x N! - y N!
         vvv
    N!^2 = xy - x N! - y N! + N!^2
         vvv
    N!^2 = (x - N!) (y - N!)

Therefore each solution (x', y') will be associated
to one and only one divisor d of N!^2, and:

        x' = d - N!   and   y' = N!^2/d + N!

Therefore the problem can be rephrased as "find the
of number of divisors (a.k.a. factors) of N!^2".

To answer this, use the following:
    i) Prime number decomposition theorem:
        Every integer M is the product of powers of prime numbers

            M = p1^k1 x p2^k2 x ... x pj^kj

        Where pi's are prime, and ki's are positive integers.

    ii) The Product Rule: the total number of factors of M equals:

        (1 + k1) x (1 + k2) x ... x (1 + kj)

    iii) Observe that if

            M = p1^k1 x p2^k2 x ... x pj^kj

         then

            M^2 = p1^(2*k1) x p2^(2*k2) x ... x pj^(2*kj)

         hence the total number of factors of M^2 equals:

            (1 + 2 k1) x (1 + 2 k2) x ... x (1 + 2 kj)

Finally, the prime factorialization of N! is the sum of
prime factorialization of 1, ... , N
'''

def product(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

def prime_factorization(N):

    assert(N<=1000000)

    PRIMES=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997]

    def primes(N):
        for prime in PRIMES:
            if not N%prime:
                return (prime, N//prime)
        return (1, N)

    primes_ = collections.defaultdict(int)
    finished = False
    while not finished:
        (i, N) = primes(N)
        if i == 1:
            finished = True
            if N != 1:
                primes_[N] += 1
        else:
            primes_[i] += 1

    return dict(primes_)


if __name__ == "__main__":

    N = int(sys.stdin.readline())

    factorizations = [prime_factorization(i) for i in range(2, N+1)]

    primes = collections.defaultdict(int)
    for factorization in factorizations:
        for prime in factorization:
            primes[prime] += factorization[prime]

    print(product([(1+2*k) for k in primes.values()])%1000007)

