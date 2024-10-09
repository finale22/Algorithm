import sys

n = int(sys.stdin.readline())
lst = []
for i in range(n):
    x, y = map(int, input().split())
    lst.append([y, x])

lst.sort()
for i in lst:
    y, x = i
    print(x, y)
