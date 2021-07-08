# sum of list
def sum(num):
  s = 0
  for i in range(len(num)):
    s = s + int(num[i])
  return s

print(sum(input().split()))