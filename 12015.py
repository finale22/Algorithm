import sys
from bisect import bisect_left

n = int(sys.stdin.readline())
arr = list(map(int, input().split()))
bs_arr = []

for i in arr:
    pos = bisect_left(bs_arr, i)
    if pos == len(bs_arr):
        bs_arr.append(i)
    else:
        bs_arr[pos] = i

print(len(bs_arr))
