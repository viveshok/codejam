#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
#import math
#import collections

WEIGHTS_VALUES = None

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


def max_duffel_bag_value(cake_tuples, capacity):

    cake_tuples = [cake for cake in cake_tuples if cake != (0, 0)]

    if any([w==0 for (w, v_) in cake_tuples]):
        return sys.maxsize

    @memoize
    def knapsack(capacity):

        if all([capacity < w for (w, v) in cake_tuples]):
            # no more space for another item
            return 0

        candidates = [v + knapsack(capacity-w) for (w, v) in cake_tuples if w<=capacity]

        return max(candidates)

    for i in range(capacity):
        # prepopulate value cache
        knapsack(i)

    return knapsack(capacity)

if __name__ == "__main__":

    cake_tuples = [(7, 160), (0, 90), (2, 15)]
    capacity = 20
#    capacity = 0

    print("value: {}".format(max_duffel_bag_value(cake_tuples, capacity)))

