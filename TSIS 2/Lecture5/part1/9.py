
# Write a Python program to count the number of lines in a text file
f = open("qwerty.txt")

c = 0
for i in f.read().split("\n"):
    if i:
        c = c + 1
print(c)