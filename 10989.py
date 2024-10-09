import sys

n = int(sys.stdin.readline())
lst = [0] * 10001

for i in range(n):
    m = int(sys.stdin.readline())
    lst[m] += 1

for i, e in enumerate(lst):
    if e != 0:
        for j in range(e):
            print(i)
