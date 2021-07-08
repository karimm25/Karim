#Write a Python program to write a list to a file.
f = open("qwerty.txt","a")

l = ['q','w','e','r','t','y']
f.write("\n")
for i in l:
    f.write(i)

f.close()

f = open("qwerty.txt", "r")
print(f.read())