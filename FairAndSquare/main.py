
import pickle

if __name__ == "__main__":

    FaSs = pickle.load(file("cache.p"))

#    finput = open("/home/alexandre/codejam/FairAndSquare/sample.in", 'r')
#    foutput = open("/home/alexandre/codejam/FairAndSquare/sample.out", 'w')

    finput = open("/home/alexandre/codejam/FairAndSquare/C-small-attempt0.in", 'r')
    foutput = open("/home/alexandre/codejam/FairAndSquare/C-small-attempt0-test.out", 'w')

#    finput = open("/home/alexandre/codejam/FairAndSquare/C-large-2.in", 'r')
#    foutput = open("/home/alexandre/codejam/FairAndSquare/C-large-2.out", 'w')


    num_cases = int(finput.readline())

    for case in range(num_cases):

        [A, B] = [int(X) for X in finput.readline().split()]

        hits = [X for X in FaSs if X>=A and X<=B]

        foutput.write("Case #"+str(case+1)+": "+str(len(hits))+"\n")

    finput.close()
    foutput.close()

