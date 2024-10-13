import sys

n = int(sys.stdin.readline())
n_lst = list(map(int, input().split()))
m = int(sys.stdin.readline())
m_lst = list(map(int, input().split()))

memo = {}
for i in m_lst:
    memo[i] = 0

keys = memo.keys()

for i in n_lst:
    if i not in keys:
        continue
    else:
        memo[i] += 1

for i in m_lst:
    print(memo[i], end=' ')
