#!/usr/bin/python3

import sys

################### trampolined solution #####################################

import types

def trampoline(generator, *args, **kwargs):
    g = generator(*args, **kwargs)
    while isinstance(g, types.GeneratorType):
        g = g.__next__()
    return g

def collatz(N, acc=1):
    if N==1:
        yield acc
    elif N%2==0:
        yield collatz(N//2, acc+1)
    else:
        yield collatz(3*N+1, acc+1)

if __name__ == "__main__":
    for i in range(1, 1000000):
        print("The Collatz cycle length of", i, "is", trampoline(collatz, i))

################### memoized solution #####################################

#import traceback
#
#def memoize(function):
#    cache = dict()
#    def memoized_function(*args):
#        print(len(traceback.extract_stack()), end="-")
#        if args in cache:
#            return cache[args]
#        else:
#            result = function(*args)
#            cache[args] = result
#            return result
#    return memoized_function
#
#@memoize
#def collatz(N, acc=1):
#    print(len(traceback.extract_stack()), end="-")
#    if N==1:
#        return acc
#    elif N%2==0:
#        return collatz(N//2, acc+1)
#    else:
#        return collatz(3*N+1, acc+1)
#
#if __name__ == "__main__":
#    for i in range(1, 52527): # blow stack at 52527
#        print("The Collatz cycle length of", i, "is", collatz(i))

