#!/usr/bin/python3

# Delete a node from a singly-linked list,
# given only a variable pointing to that node.

import sys
#import math
#import collections

class Node():
    def __init__(self, val):
        self.value = val
        self.next = None
    def print(self):
        print(self.value, end=", ")
        if self.next:
            self.next.print()
        else:
            print()

def delete_node(b):
    if b.next:
        b.value = b.next.value
        b.next = b.next.next
    else:
        raise "can't delete last node with this method"

if __name__ == "__main__":

    a = Node('A')
    b = Node('B')
    c = Node('C')
    a.next = b
    b.next = c
    a.print()
    delete_node(b)
    a.print()

