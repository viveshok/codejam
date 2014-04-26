
# trampoline

import types

def trampoline(generator, *args, **kwargs):
    g = generator(*args, **kwargs)
    while isinstance(g, types.GeneratorType):
        g = g.__next__() # python 3
        #g = g.next() # python 2
    return g

# memoization

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

# product of list

def product(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

