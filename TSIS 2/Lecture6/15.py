# Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.

def sort_(n):
    seq = n.split('-')
    seq.sort()
    print('-'.join(seq))

sort_(input())