# https://www.hackerrank.com/challenges/re-group-groups/problem
# Group(), Groups() & Groupdict()
import re
m = re.findall(r"([A-Za-z0-9])\1+",input())
if m:
    print(m[0])
else:
    print(-1)