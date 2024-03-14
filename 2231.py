import sys

n = int(sys.stdin.readline())
res = 0
for i in range(n):
    tmp1 = i
    tmp2 = 0
    for j in str(i):
        tmp2 += int(j)
    if tmp1 + tmp2 == n:
        res = i
        break

print(res)
