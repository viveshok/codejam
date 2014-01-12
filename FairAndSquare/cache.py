
import pickle

if __name__ == "__main__":

    FaSs = [1L,4L,9L]

    for i in range(0,48):
        buf = i*"0"
        string = "4" + buf + "8" + buf + "4"
        FaSs.append(long(string))

    i = 1
    while i <= 33554431:
        num_string = bin(i)[2:]
        num = long(num_string + num_string[::-1])
        square = num*num
        square_string = str(square)
        if square_string == square_string[::-1]:
            FaSs.append(square)
            print num, square
        i += 1

    pickle.dump(FaSs, file("cache.p", "w"))
    print FaSs

