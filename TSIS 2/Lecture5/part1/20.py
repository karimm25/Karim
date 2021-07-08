# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
import string

for i in string.ascii_uppercase:
   f = open(i + ".txt","a")
   f.write(i)
    