#  Write a Python program to read a file line by line store it into a variable.
f = open("qwerty.txt","r")
str=""
for i in f.read():
    str = str + i
print(str)