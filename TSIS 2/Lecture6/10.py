# program to print the even numbers from a given list
def only_even(l):
    for i in l:
        if int(i)%2 == 0:
            pass
        else:
            l.remove(i)
    print(l)

only_even(input().split())