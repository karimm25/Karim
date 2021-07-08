# Write a Python program that takes a text file as input and returns the number of words of a given text file
f = open("qwerty.txt")

words = f.read().split()

print(len(words))