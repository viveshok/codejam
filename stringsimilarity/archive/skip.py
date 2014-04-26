
import sys

num_cases = int(sys.stdin.readline())

for case in range(num_cases):

    string = sys.stdin.readline().rstrip('\n')
    hd = string[0]
    len_string = len(string)

    i = 1
    accum = len_string
    while i<len_string:
        skip = 1
        for j in range(len_string-i):
            if string[i+j] != string[j]:
                break
            elif skip == 1 and j>1 and string[i+j] == hd:
                skip = j
            accum += 1
        i += skip

    print(accum)

