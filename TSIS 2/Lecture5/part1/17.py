#  Write a Python program to remove newline characters from a file.
f = open("qwerty.txt","r")

lines = f.read().splitlines()

f.close()
f = open("qwerty.txt","w")

x = ' '
for i in lines:
    f.write(i)
    f.write(x)