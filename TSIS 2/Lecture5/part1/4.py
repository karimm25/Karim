#Write a Python program to read last n lines of a file.
f = open("qwerty.txt")

l = f.read().split("\n")
print(l[-int(input()):])