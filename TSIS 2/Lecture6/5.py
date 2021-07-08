# function to calculate the factorial of a number
def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n - 1)

print(fac(int(input())))