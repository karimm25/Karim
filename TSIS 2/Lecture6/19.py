# Write a Python program to access a function inside a function
def q(a):
    def w(b):
         nonlocal a
         return a + 10 + b
    return w

f = q(10)
print(f(10))