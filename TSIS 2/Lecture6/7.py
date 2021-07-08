#  function that accepts a string and calculate the number of upper case letters and lower case letters
def up_and_down (s):
    u = 0
    d = 0
    for i in s:
        if i.isupper():
            u = u + 1
        elif i.islower():
            d = d + 1
    return u , d

print(up_and_down(input()))