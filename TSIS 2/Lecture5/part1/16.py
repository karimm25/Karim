
 # Write a Python program to assess if a file is closed or not.

f = open("qwerty.txt")

print(f.closed)
f.close()
print(f.closed)