
# trampoline ##########################

import types

def trampoline(generator, *args, **kwargs):
    g = generator(*args, **kwargs)
    while isinstance(g, types.GeneratorType):
        g = g.__next__() # python 3
        #g = g.next() # python 2
    return g

# memoization ########################

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

# product of list ####################

def product(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

# Sieve of Eratosthenes ##############

def primes(N):

    def find(start_index, bool_list):
        for i in range(start_index, len(bool_list)):
            if bool_list[i]:
                return i

        return False

    ledger = [False, False] + [True] * N
    primes_ = list()
    prime = 2
    finished = False
    while not finished:
        prime = find(prime, ledger)
        if prime:
            primes_.append(prime)
            for i in range(prime, N+2, prime):
                ledger[i] = False
        else:
            finished = True

    return primes_

# Prime factorization ################

import collections
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


# main #################################

if __name__ == "__main__":
    print(prime_factorization(3))
    print(prime_factorization(1009))

