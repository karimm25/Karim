# Write a Python program to count the frequency of words in a file.

f = open("qwerty.txt")

m = []
q = f.read().split()
for i in q:
    m.append(q.count(i))
print(zip(q,m))