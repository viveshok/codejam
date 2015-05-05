#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
#import math
#import collections

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def set_left(self, l):
        self.left = l

    def set_right(self, r):
        self.right = r

    def traverse(self):
        if self.left:
            self.left.traverse()
        print(self.val, end=" ")
        if self.right:
            self.right.traverse()

    def swap(self, i, K):
        if i == K:
            tmp = self.left
            self.left = self.right
            self.right = tmp
            i = 0
        if self.left:
            self.left.swap(i+1, K)
        if self.right:
            self.right.swap(i+1, K)

if __name__ == "__main__":

    # try to come up with iterative instead
    # of recursive solution to stop blowing
    # the stack
    sys.setrecursionlimit(2000)

    N = int(sys.stdin.readline())
    nodes = [Node(i) for i in range(1, N+1)]
    for node in nodes:
        [left, right] = [int(X) for X in sys.stdin.readline().split()]
        if left != -1:
            node.set_left(nodes[left-1])
        if right != -1:
            node.set_right(nodes[right-1])

    root = nodes[0]

    T = int(sys.stdin.readline())
    for case in range(T):
        K = int(sys.stdin.readline())
        root.swap(1, K)
        root.traverse()
        print()

