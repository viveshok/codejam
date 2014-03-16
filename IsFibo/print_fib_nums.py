
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
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    print("\nFIB = {", end="")
    i = 0
    while fib(i) <= 100000000000:
        print(fib(i), ",", sep="", end="")
        i += 1
    print("\x08}\n")

