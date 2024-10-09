import sys

n = int(sys.stdin.readline())
lst = []

for i in range(n):
    age, name = map(str, input().split())
    date = i
    lst.append([int(age), i, name])

lst.sort()

for i in lst:
    age, _, name = i
    print(age, name)
