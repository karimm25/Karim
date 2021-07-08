# print a list where the values are square of numbers between 1 and 30 (both included)

import math

def sqr130():
    l = list()
    for i in range(1,31):
        l.append(pow(i,2))
    print(l)
sqr130()