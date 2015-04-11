#!/usr/bin/python3

import sys
#import math
#import collections

SOLNS = {():0, (1):1}

def possible_splits(stack):
    start = stack//2 if stack%2==0 else stack//2+1
    return [(i, stack-i) for i in range(start, stack-1)]

def insert_stack(stack, pancakes):
    for (i, s) in enumerate(pancakes):
        if stack >= s:
            pancakes.insert(i, stack)
            return pancakes

    pancakes.append(stack)
    return pancakes

def insert_stacks(stacks, pancakes):
    (stack1, stack2) = stacks
    pancakes = insert_stack(stack2, pancakes)
    pancakes = insert_stack(stack1, pancakes)
    return pancakes

def possible_scenarii(splits, pancakes):
    return [insert_stacks(split, pancakes.copy()) for split in splits]

def solve(pancakes):

    key = tuple(pancakes)
    if key in SOLNS:
        return SOLNS[key]

    max_stack = pancakes.pop(0)

    if max_stack >= 4:
        splits = possible_splits(max_stack)
        scenarii = possible_scenarii(splits, pancakes)
        soln = min(max_stack, 1 + min([solve(scenario) for scenario in scenarii]))
    else:
        soln = max_stack

    SOLNS[key] = soln
    return soln

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        num_diners = int(sys.stdin.readline())

        pancakes = sorted([int(X) for X in sys.stdin.readline().split()], reverse=True)
        if pancakes[0] <= 3:
            soln = pancakes[0]
        else:
            pancakes = [p for p in pancakes if p > 1] # remove trailing 1s
            soln = solve(pancakes)

        print("Case #", case+1, ": ", soln, sep="")

