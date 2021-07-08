#  Write a Python program to create a file where all letters of English alphabet are listed by specified number of letters on each line
import string

n = int(input())

f = open("A.txt","a")
alphabet = string.ascii_uppercase
lines = []

for i in range(0, len(alphabet), n):
    lines.append(alphabet[i:i+3])

for i in lines:
    f.write(i+"\n")
f.close()
