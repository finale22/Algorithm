import sys

s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()
dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
for i in range(len(s1) + 1):
    for j in range(len(s2) + 1):
        if i == 0 or j == 0:
            continue
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

ans = 0
for lst in dp:
    ans = max(ans, max(lst))

print(ans)
