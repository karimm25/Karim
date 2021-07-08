# Write a python program to find the longest words
f = open("qwerty.txt")

words = f.read().split()
print(words)
print( len(max(words)))