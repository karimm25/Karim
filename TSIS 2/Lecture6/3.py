def multiple_list(num):
    total = 1
    for i in range(len(num)):
        total = total * int(num[i])
    return total

print(multiple_list(input().split()))