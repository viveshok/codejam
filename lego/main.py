
import sys

MODULO = 1000000007

def memoize(function): 
    '''
    Simply a decorator to memoize
    the results of a function
    '''
    cache = dict()
    def memoized_function(*args):
        if args in cache:
            return cache[args]
        else:
            result = function(*args)
            cache[args] = result
            return result
    return memoized_function

if __name__ == '__main__':

    # array that will hold different possibilities for
    # a single layer of bricks (N=1, M=1...1000)
    single_layer = [-1] * 1001 
    single_layer[1:5] = [1, 2, 4, 8]
    for i in range(5, 1001):
        single_layer[i] = single_layer[i-1] + single_layer[i-2] + \
                              single_layer[i-3] + single_layer[i-4]


    exp = memoize(pow) # memoized exponential function

    @memoize
    def soft_walls(N, M):
        '''
        Returns how many NxM "soft" walls are possible
        '''
        result = 0 
        for i in range(1, M):
            result += solid_walls(N, i) * exp(single_layer[M-i], N, MODULO)
            result %= MODULO
        return result

    @memoize
    def solid_walls(N, M):
        '''
        Returns how many NxM "solid" walls are possible
        '''
        if N == 1:
            return 0 if M > 4 else 1
        else:
            return (exp(single_layer[M], N, MODULO) - soft_walls(N, M))%MODULO
    
    num_cases = int(sys.stdin.readline())

    for case in range(num_cases):
        N, M = (int(X) for X in sys.stdin.readline().split())
        print(solid_walls(N, M))

