# Write a Python program to read a file line by line store it into an array.

f =open("qwerty.txt")
array = []

for i in f.read().split("\n"):
    array.append(i)

print(array)