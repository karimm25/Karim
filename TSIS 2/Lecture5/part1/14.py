# Write a Python program to combine each line from first file with the corresponding line in second file.
f1 = open("qwerty.txt")
f2 = open("qwerty_1.txt")

lines1 = f1.read().split("\n")
lines2 = f2.read().split("\n")

f3 = open("qwerty_2.txt","a")

for i in (tuple(zip(lines1,lines2))):
    f3.write(str(i))
    f3.write("\n")

f1.close()
f2.close()
f3.close()