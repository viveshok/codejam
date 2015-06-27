#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
#import math
#import collections

class Segment():
    # direction: -1 -> decreasing, 0 -> neither, 1 -> increasing

    def __init__(self, direction, head):
        self.content = [head]
        self.direction = direction
        self.min_ = head
        self.max_ = head

    def append(self, item):
        self.content.append(item)
        self.min_ = item if item<self.min_ else self.min_
        self.max_ = item if item<self.max_ else self.max_

    def __str__(self):
        fmt = "direction: {} min: {} max: {}"
        return fmt.format(self.direction, self.min_, self.max_)

def chop_segment(ds):

    if len(ds) == 1:
        return (Segment(0, ds[0]), [])

    if len(ds) == 2:
        segment = Segment(1 if ds[0] < ds[1] else -1, ds[0])
        segment.append(ds[1])
        return (segment, [])

    if ds[0] < ds[1] < ds[2]:
        segment = Segment(1, ds[0])
    elif ds[0] < ds[1] > ds[2]:
        return (Segment(0, ds[0]), ds[1:])
    else:
        segment = Segment(-1, ds[0])

    i = 1
    while i < len(ds)-1:
        if segment.direction == 1:
            if ds[i] < ds[i+1]:
                segment.append(ds[i])
            else:
                return (segment, ds[i:])
        elif segment.direction == -1:
            segment.append(ds[i])
            if ds[i] < ds[i+1]:
                return (segment, ds[i+1:])
        i += 1

    segment.append(ds[i])
    return (segment, [])

def get_segments(ds):
    segments = list()
    count = 0
    while ds:
        (segment, ds) = chop_segment(ds)
        segments.append(segment)
        count += 1
        if count > 5:
            return False
    return segments

def solve(segments):

    for s in segments:
        print(s)

    # first check if array is already sorted
    if len(segments) == 1 and segments[0].direction != -1:
        print("yes")
        return

    # second check if it's possible to reverse one segment
    num_reversed = sum([s.direction == -1 for s in segments])
    if num_reversed == 1:
        i = 1
        segments_ordered = True
        while i < len(segments):
            if segments[i-1].max_ > segments[i].min_:
                segments_ordered = False
                break
            i += 1
        if segments_ordered:
            print("yes")
            # TODO
            print("reverse {} {}".format("?", "?"))
            return

    # finally check if possible to swap two 1-long segments
    # TODO
    # if ...
    # ...
    # return

    print("no")

if __name__ == "__main__":

    _N = int(sys.stdin.readline())

    ds = [int(X) for X in sys.stdin.readline().split()]

    segments = get_segments(ds)

    if segments:
        solve(segments)
    else:
        print("no")

