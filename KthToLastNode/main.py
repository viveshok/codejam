#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
#import math
#import collections

class Node():
    def __init__(self, val):
        self.value = val
        self.next = None

def kth_to_last_node(k, node):
    ptr = node
    while k > 0:
        ptr = ptr.next
        if not ptr:
            raise "linked list not long enough"
        k -= 1
    while ptr:
        node = node.next
        ptr = ptr.next
    return node


if __name__ == "__main__":

    a = Node("Angel Food")
    b = Node("Bundt")
    c = Node("Cheese")
    d = Node("Devil's Food")
    e = Node("Eccles")

    a.next = b
    b.next = c
    c.next = d
    d.next = e

    print(kth_to_last_node(2, a).value)

