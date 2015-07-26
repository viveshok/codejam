#!/usr/bin/python3

# how to
# $ python3 -m doctest -v main.py # to test
# $ ./main.py < input > output # to run

import sys
#import math
#import collections

def num_ones(cumulative_binary, left, right):
    if left < 0:
        left = 0
    if right > len(cumulative_binary):
        right = len(cumulative_binary) - 1
    if left > right:
        return 0
    return cumulative_binary[right] - (cumulative_binary[left-1] if left > 0 else 0)

if __name__ == "__main__":

    N = 314159
    MOD = 1000000007

    A = sys.stdin.readline().strip()
    B = sys.stdin.readline().strip()

    NMax = 1000000
    A = '0' * (NMax-len(A)) + A
    B = '0' * (NMax-len(B)) + B

    power_mod = [1]
    for i in range(NMax-1):
        power_mod.append((2 * power_mod[i]) % MOD)

    count = 0
    sb = []
    for i in range(NMax-1, -1, -1):
        count += 1 if B[i] == '1' else 0
        sb.append(count)

    ans = 0
    for i in range(NMax):
        if A[NMax-1-i] == '1':
            ans += power_mod[i] * (N - num_ones(sb, i-N, i) + 1)
        else:
            ans += power_mod[i] * num_ones(sb, i-N, i)

    print(ans % MOD)

