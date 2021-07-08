
#  Write a Python program to copy the contents of a file to another file .

f = open("qwerty.txt","a")
f1 = open("qwerty_1.txt")

words = f1.readlines()

for i in words:
    f.write(i)

f.close()
f1.close()

f = open("qwerty.txt")
print(f.read())