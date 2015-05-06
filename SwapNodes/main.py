#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
#import math
#import collections

def step(node):
    left = traverse(node.left)
    left.append(node.val)
    right = traverse(node.right)
    left.extend(right)
    return left

def traverse(node):
    if node:
        return step(node)
    else:
        return []

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
        left = self.left.traverse() if self.left else []
        left.append(self.val)
        right = self.right.traverse() if self.right else []
        left.extend(right)
        return left

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
    # the stack - consult:
    # http://blog.moertel.com/posts/2013-06-03-recursion-to-iteration-3.html
    sys.setrecursionlimit(4000)

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

        vals = traverse(root)
#        vals = root.traverse()

        for val in vals:
            print(val, end=" ")
        print()

