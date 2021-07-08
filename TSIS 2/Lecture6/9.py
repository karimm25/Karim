#  Write a Python function that takes a number as a parameter and check the number is prime or not
import math
def if_prime(n):
    for i in range(2,int(math.sqrt(n))):
        if n % i > 0:
            return False
    return True

if if_prime(int(input())):
    print("it is prime")
else:
    print("not")