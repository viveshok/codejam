#!/usr/bin/python3

# $ python3 -m doctest -v main.py # to test

"""
reverse words of a string in place
now since python strings are immutable,
fake it with char arrays
"""

def reverse_word(i, j, chr_array):
    for k in range((j+1-i)//2):
        chr_array[j-k] += chr_array[i+k]
        chr_array[i+k] = chr_array[j-k] - chr_array[i+k]
        chr_array[j-k] -= chr_array[i+k]

def reverse_words(string):
    """
    overall strategy:
    (i) reverse words in place one by one
    (ii) reverse whole string in place
    >>> reverse_words('find you will pain only go you recordings security the into if')
    'if into the security recordings you go only pain will you find'
    """
    chr_array = [ord(c) for c in string]
    i, j = 0, 0
    while i < len(string):
        while j < len(string) and chr_array[j] != 32:
            j += 1
        reverse_word(i, j-1, chr_array)
        j += 1
        i = j
    reverse_word(0, len(string)-1, chr_array)
    return ''.join([chr(c) for c in chr_array])

if __name__ == "__main__":
    print(reverse_words('find you will pain only go you recordings security the into if'))

