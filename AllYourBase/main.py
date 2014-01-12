#!/usr/bin/python

import sys

DIGITS = ['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a','9','8','7','6','5','4','3','2','0']

def unique(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if x not in seen and not seen_add(x)]

if __name__ == "__main__":

#    finput = open("sample.in", 'r')
#    foutput = sys.stdout

#    finput = open("small.in", 'r')
#    foutput = open("small.out", 'w')

    finput = open("large.in", 'r')
    foutput = open("large.out", 'w')

    num_cases = int(finput.readline())

    for case in range(num_cases):

        number = finput.readline()[:-1]
        #print "number: ", number
        symbols = unique(number)
        #print "symbols: ", symbols
        base = len(symbols)
        base = base if base>1 else 2
        #print "base: ", base
        digits = DIGITS[1-base:]
        #print "digits: ", digits
        tmp = zip(reversed(symbols), digits)
        mapping = dict(tmp)
        #print "mapping: ", mapping
        mapping[symbols[0]] = '1'
        #print "mapping: ", mapping
        decrypted = ''.join([mapping[symbol] for symbol in number])
        #print "decrypted: ", decrypted
        result = int(decrypted, base)
        #print "result: ", result

        foutput.write("Case #"+str(case+1)+": "+str(result)+"\n")

    finput.close()
    foutput.close()

