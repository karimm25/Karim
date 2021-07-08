# https://www.hackerrank.com/challenges/introduction-to-regex/problem
# Detect Floating Point Number
import re

quantity = int(input())

for i in range(quantity):
    num = input()
    x = re.match(r"^[-+]?[0-9]*\.[0-9]+$", num)
    if x:
        print("True")
    else:
        print("False")    
# ^ begin
# [-+]? one of this or nothing
# [0-9]* 0 or infinty times of dig
# \. matches "."
# [0-9]+ 1 or infinty times
# $ end of word