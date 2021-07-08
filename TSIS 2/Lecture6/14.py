#  check whether a string is a pangram or not
import string, sys

def pan(str_):
    alphaset = set(string.ascii_lowercase)
    return alphaset <= set(str_)

print(pan(input())) 