import sys
n = int(sys.stdin.readline())
end = 10 ** n
dp = [[0] * 12 for _ in range(n)]
for i in range(1, 10):
    dp[0][i + 1] = 1
for digit in range(n - 1):
    for m in range(1, 11):
        dp[digit + 1][m] = dp[digit][m - 1] + dp[digit][m + 1]
print(sum(dp[n - 1]) % 1000000000)
