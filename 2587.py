import sys

n = 5
lst = []

for i in range(n):
    lst.append(int(sys.stdin.readline()))

lst.sort()

print(sum(lst) // 5)
print(lst[n//2])
