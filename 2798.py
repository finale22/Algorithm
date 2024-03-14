from itertools import combinations
import sys

n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

combination = list(combinations(cards, 3))
res = 0
for c in combination:
    s = sum(c)
    if (res <= s) & (s <= m):
        res = s

print(res)
