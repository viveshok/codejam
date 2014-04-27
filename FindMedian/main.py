#!/usr/bin/python3

import sys

def kth(array, k):

    assert(array)

    less = list()
    greater = list()

    pivot = array.pop()

    for x in array:
        if x < pivot:
            less.append(x)
        else:
            greater.append(x)

    if len(less) == k-1:
        return pivot
    elif len(less) >= k:
        return kth(less, k)
    else:
        return kth(greater, k-len(less)-1)


if __name__ == "__main__":

#    #<some tests>====================================================
#    import random
#
#    for i in range(10):
#        max_N = 1000001
#        N = random.randint(1, max_N)
#        N += N%2+1 # to make sure odd number of elements
#        array = [random.randint(-10000, 10000) for i in range(N)]
#        sorted_array = sorted(array)
#        if kth(array, len(array)//2+1) == sorted_array[len(sorted_array)//2]:
#            print(".", end="")
#        else:
#            print("TEST FAIL!")
#            break
#    #</ some tests>==================================================

    N = int(sys.stdin.readline())

    array = [int(X) for X in sys.stdin.readline().split()]

    print(kth(array, len(array)//2+1))

