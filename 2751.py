import sys

n = int(sys.stdin.readline())
lst = []
for i in range(n):
    m = int(sys.stdin.readline())
    lst.append(m)

lst.sort()
for i in lst:
    print(i)
