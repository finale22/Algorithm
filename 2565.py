import sys
from bisect import bisect_left

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
arr.sort()
dp = [501]
for _, b in arr:
    idx = bisect_left(dp, b)
    if idx < len(dp):
        dp[idx] = b
    else:
        dp.append(b)

ans = n - len(dp)
print(ans)
