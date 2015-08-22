#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
#import math
#import collections

def validate(string):
    """
    >>> validate("{[]()}")
    True
    >>> validate("{[(])}")
    False
    >>> validate("{ [ }")
    False
    >>> validate("{al[fdsf] sdff  ( fdsffd) sdff} sdf")
    True
    """
    opening_brackets = {'(', '{', '['}
    closing_brackets = {')':'(', ']':'[', '}':'{'}
    brackets_stack = list()
    for char in string:
        if char in closing_brackets:
            if not brackets_stack:
                return False
            elif brackets_stack.pop() != closing_brackets[char]:
                return False
        elif char in opening_brackets:
            brackets_stack.append(char)
    return not brackets_stack

