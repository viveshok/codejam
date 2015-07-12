#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
import bisect

RED = 31
GREEN = 32
ESCAPE = '%s[' % chr(27)
RESET = '%s0m' % ESCAPE
FORMAT = '1;%dm'

def colorize(text, color):
    return ESCAPE + (FORMAT % (color, )) + text + RESET

def prefix_sum(xs, modulo):
    cumsum = 0
    result = list()
    for x in xs:
        cumsum = (cumsum + x) % modulo
        result.append(cumsum)
    return result

def solve(xs, M):

#    print("M = {}".format(M))
#
#    prefix_sum_ = prefix_sum(xs, sys.maxsize)
#    maximum = -sys.maxsize
#    I = -1
#    J = -1
#    for i in range(len(prefix_sum_)):
#        for j in range(i, len(prefix_sum_)):
#            if (prefix_sum_[j]-prefix_sum_[i])%M > maximum:
#                maximum = (prefix_sum_[j]-prefix_sum_[i])%M
#                I = i
#                J = j
#
#    print("\n")
#
#    for i, x in enumerate(xs):
#        if i in [I, J]:
#            print(colorize(str(x), GREEN), end=" ")
#        else:
#            print(x, end=" ")
#
#    print("\n")
#
#    for i, s in enumerate(prefix_sum_):
#        if i in [I, J]:
#            print(colorize(str(s), GREEN), end=" ")
#        else:
#            print(s, end=" ")
#
#    print("\n")
#    print(maximum)
#    print("\n")
#
#    cumsums = prefix_sum(xs, M)
#
#    for i, s in enumerate(cumsums):
#        if i in [I, J]:
#            print(colorize(str(s), GREEN), end=" ")
#        else:
#            print(s, end=" ")
#
#    print("\n")

    cumsum = xs[0]
    cumsums = [cumsum]
    maximum = -sys.maxsize

    for j,x in enumerate(xs[1:]):
        cumsum = (cumsum + x) % M
        candidate_index = bisect.bisect(cumsums, (cumsum-M) % M)

#        print("cumsum: {} cumsums: {}".format(cumsum, cumsums))
#        print("candidate_index: {}".format(candidate_index))
#        sys.stdout.flush()

        if candidate_index < len(cumsums):
            maximum = max(maximum, (cumsum-cumsums[candidate_index]) % M)
        bisect.insort(cumsums, cumsum)

    return maximum

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        [N_, M] = [int(X) for X in sys.stdin.readline().split()]

        xs = [int(X) for X in sys.stdin.readline().split()]

        print(solve(xs, M))

