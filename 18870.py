import sys

n = int(sys.stdin.readline())
lst = list(map(int, input().split()))
sorted_lst = sorted(list(set(lst)), reverse=True)
d = {}

for i, e in enumerate(sorted_lst):
    d[e] = len(sorted_lst) - i - 1

for i in lst:
    print(d[i], end=' ')
