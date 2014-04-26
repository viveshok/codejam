#!/usr/bin/python3

import sys
import random

def bad_swap(array):
    for i, v in enumerate(array):
        p = random.randint(0, len(array)-1)
        tmp = array[i]
        array[i] = array[p]
        array[p] = tmp

    return array

def good_swap(array):
    for i, v in enumerate(array):
        p = random.randint(i, len(array)-1)
        tmp = array[i]
        array[i] = array[p]
        array[p] = tmp

    return array

if __name__ == "__main__":

    T = 120

#    ### good 
#
#    f_good = open("good.in", 'w')
#
#    f_good.write(str(T) + '\n')
#
#    for i in range(T):
#
#        f_good.write("1000\n")
#
#        for v in good_swap(list(range(1000))):
#            f_good.write(str(v) + " ")
#
#        f_good.write("\n")
#
#    f_good.close()
#
#    ### bad 
#
#    f_bad = open("bad.in", 'w')
#
#    f_bad.write(str(T) + '\n')
#
#    for i in range(T):
#
#        f_bad.write("1000\n")
#
#        for v in bad_swap(list(range(1000))):
#            f_bad.write(str(v) + " ")
#
#        f_bad.write("\n")
#
#    f_bad.close()

    ### test 

    f_test = open("test.in", 'w')

    f_test.write(str(T) + '\n')

    for i in range(T//2):

        f_test.write("1000\n")

        for v in good_swap(list(range(1000))):
            f_test.write(str(v) + " ")

        f_test.write("\n")

    for i in range(T//2):

        f_test.write("1000\n")

        for v in bad_swap(list(range(1000))):
            f_test.write(str(v) + " ")

        f_test.write("\n")

    f_test.close()

