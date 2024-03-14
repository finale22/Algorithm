import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
dq = deque()
for i in range(n):
    dq.append(int(sys.stdin.readline()))

res = 0
for i in range(len(dq)):
    money = dq.pop()
    if money <= k:
        tmp = k // money
        res += tmp
        k -= money * tmp

print(res)
