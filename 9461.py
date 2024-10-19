import sys

t = int(sys.stdin.readline())
dp = [1, 1, 1, 2, 2]
n_arr = []

for _ in range(t):
    n = int(sys.stdin.readline())
    n_arr.append(n)

max_n = max(n_arr)

if max_n > 5:
    for i in range(5, max_n):
        dp.append(dp[i - 1] + dp[i - 5])

for i in n_arr:
    print(dp[i - 1])
