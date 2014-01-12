
def min_length(lawn):
    return min([min(X) for X in lawn])

def max_length(lawn):
    return max([max(X) for X in lawn])

def uncut(lawn, length):
    N = len(lawn)
    M = len(lawn[0])
    new_lawn = list()

    for i, row in enumerate(lawn):
        if all([x==length for x in row]):
            new_lawn.append(list(M*[length+1]))
        else:
            new_lawn.append(list(row))

    for i in range(M):
        col = [row[i] for row in lawn]
        if all([x==length for x in col]):
            for j in range(N):
                new_lawn[j][i] = length+1

    return new_lawn

if __name__ == "__main__":

    finput = open("/home/alexandre/codejam/Lawnmower/B-large.in", 'r')
    foutput = open("/home/alexandre/codejam/Lawnmower/B-large.out", 'w')

    num_cases = int(finput.readline())

    for case in range(num_cases):
        [N, M] = [int(X) for X in finput.readline().split()]

        lawn = list(list())
        for row in range(N):
            lawn.append([int(X) for X in finput.readline().split()])

        for length in range(min_length(lawn), max_length(lawn)):
            lawn = uncut(lawn, length)

        lawn = set([item for sublist in lawn for item in sublist])
        if len(lawn) == 1: # feasible
            foutput.write("Case #" + str(case+1) + ": YES\n")
        else: 
            foutput.write("Case #" + str(case+1) + ": NO\n")

    finput.close()
    foutput.close()

