import sys
from bisect import bisect_left, bisect_right

n = int(sys.stdin.readline())
n_lst = list(map(int, input().split()))
m = int(sys.stdin.readline())
m_lst = list(map(int, input().split()))

n_lst.sort()

for i in m_lst:
    left = bisect_left(n_lst, i)
    right = bisect_right(n_lst, i)
    print(right-left, end=' ')
