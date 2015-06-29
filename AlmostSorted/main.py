#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
#import math
#import collections

def is_sorted(ds):
    i = 0
    while i < len(ds)-1:
        if ds[i] > ds[i+1]:
            return False
        i += 1
    return True

def swap(i, j, ds):
    result = [d for d in ds]
    tmp = result[i]
    result[i] = result[j]
    result[j] = tmp
    return result

def solve_swap(ds):
    i = 0
    candidate_idx = None
    candidate = None
    candidate_left_neighbour = None
    candidate_right_neighbour = None

    while i<len(ds)-1:
        if not candidate and ds[i] > ds[i+1]:
            candidate_idx = i
            candidate = ds[i]
            candidate_left_neighbour = -1 if i==0 else ds[i-1]
            candidate_right_neighbour = ds[i+1]

        if candidate and ds[i] > ds[i+1]:
            if candidate_left_neighbour < ds[i+1] < candidate_right_neighbour:
                tmp = ds[i+2] if i+2<len(ds) else 1000001
                if ds[i] < candidate < tmp:
                    test = swap(candidate_idx, i+1, ds)
                    if is_sorted(test):
                        return "yes\nswap {} {}".format(candidate_idx+1, i+1+1)

        i += 1

    return False

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
        self.max_ = item if item>self.max_ else self.max_

    def __str__(self):
        fmt = "content: {} direction: {} min: {} max: {}"
        return fmt.format(self.content, self.direction, self.min_, self.max_)

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

def get_indices_reverse_segment(segments):
    count = 1
    for segment in segments:
        if segment.direction == -1:
            return (count, count+len(segment.content)-1)
        else:
            count += len(segment.content)

def solve_reverse(segments):

    # first check if array is already sorted
    if len(segments) == 1 and segments[0].direction != -1:
        return "yes"

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
            (start, stop) = get_indices_reverse_segment(segments)
            return "yes\nreverse {} {}".format(start, stop)

    return False



if __name__ == "__main__":

    _N = int(sys.stdin.readline())

    ds = [int(X) for X in sys.stdin.readline().split()]

    if len(ds) == 2:
        if ds[0] < ds[1]:
            print("yes")
        else:
            print("yes\nswap 1 2")
        exit(0)

    result = solve_swap(ds)
    if result:
        print(result)
        exit(0)

    segments = get_segments(ds)

    if segments:
        result = solve_reverse(segments)
        if result:
            print(result)
            exit(0)

    print("no")

