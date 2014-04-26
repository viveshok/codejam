
import sys

N = int(sys.stdin.readline())

for i in range(N):

    string = sys.stdin.readline().rstrip('\n')
    len_string = len(string)

    table = [len_string] + [0] * (len_string - 1)
    j = 1

    while(j<len_string):

        for k in range(len_string-j+1):
            if j+k == len_string or string[j+k] != string[k]:
                break

        table[j] = k

        if k>5:
            l = min(j, k-1)
            upper_bound = range(k-1, k-1-l ,-1)
            precomputed = table[1:l+1]
            patch = [min(a,b) for a,b in zip(upper_bound, precomputed)]

#            print("\nstring:", string)
#            print("j:",j,", k:",k,", l:",l)
#            print("upper_bound:", list(upper_bound))
#            print("precomputed:", precomputed)
#            print("patch      :", patch)
#            print()

            table[j+1:j+l+1] = patch
            j += max(1, l-3)
        else:
            j += 1

#    table_brute_force = [len_string] + [0] * (len_string-1) 
#    for j in range(1, len_string):
#        accum = 0
#        for k in range(len_string-j):
#            if string[j+k] != string[k]:
#                break
#            else:
#                accum += 1
#        table_brute_force[j] = accum

#    print(string)
#   print(','.join([str(x) for x in table]))
    print(sum(table))

#    print(','.join([str(x) for x in table_brute_force]))
#    print(list(zip(table_brute_force, table)))
#    for i, substr in enumerate(table):
#        if substr != table_brute_force[i]:
#            print(i, string[i-10:i+10])
#            print(table[i-10:i+10])
#            print(table_brute_force[i-10:i+10])
#            break

#    print(sum(table), end=", ")
#    print(sum(table_brute_force))



