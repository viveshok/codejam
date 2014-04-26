
import sys

def preprocess(virus, max_mismatch):

    len_virus = len(virus)
    for i in range(1, len_virus):
        mismatch_count = 0
        for j in range(1, len_virus-i):
            if virus[j] != virus[i+j]:
                

T = int(sys.stdin.readline())
for i in range(T):

    patient = sys.stdin.readline()
    virus = sys.stdin.readline()
    len_virus = len(virus)

    for j in range(len(patient)-len_virus+1):
        if sum(ch1 != ch2 for ch1, ch2 in zip(patient[j:j+len_virus-1], virus)) <= 1:
            print(j, end=' ')

    print('\n', end='')
    if i != T - 1 : sys.stdin.readline() 

