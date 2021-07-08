
# Write a Python program to read a random line from a file.
import random
f = open("qwerty.txt")

lines = f.read().splitlines()
print(random.choice(lines))