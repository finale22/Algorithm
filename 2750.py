import sys

n = int(sys.stdin.readline())
s = set()

for i in range(n):
    s.add(int(sys.stdin.readline()))

lst = list(s)
lst.sort()

for i in lst:
    print(i)
