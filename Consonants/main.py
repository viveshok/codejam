
import sys

def memoize(function): 
    cache = dict()
    def memoized_function(*args):
        if args in cache:
            return cache[args]
        else:
            result = function(*args)
            cache[args] = result
            return result
    return memoized_function

@memoize
def count(name, n):

    if len(name) <= n:
        return 0 if any(char in "aeiou" for char in name) else 1

    left = count(name[:-1],n)
    middle = count(name[1:-1],n)
    right = count(name[1:],n)

    left = left + 0.5*middle
    right = right + 0.5*middle

    left = left+1 if left>0 else 0
    right = right+1 if right>0 else 0

    subtree = left + right
    
    return 1+subtree if subtree>0 else 0


if __name__ == "__main__":

    finput = open("sample.in", 'r')
    foutput = sys.stdout

#    finput = open("small.in", 'r')
#    foutput = open("small.out", 'w')

#    finput = open("large.in", 'r')
#    foutput = open("large.out", 'w')

    T = int(finput.readline())

    for case in range(T):

#        print("Case", case + 1, "of", T, "...")

        name, n = tuple(finput.readline().split())
        n = int(n)

        result = int(count(name, n))

        foutput.write("Case #"+str(case+1)+": "+str(result)+"\n")

    finput.close()
    foutput.close()

