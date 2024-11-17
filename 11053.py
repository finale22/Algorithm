import sys

n = int(sys.stdin.readline())
arr = list(map(int, input().split()))
dp = [arr[0]]
for i in range(1, n):
    new = arr[i]
    flag = 0
    for j in range(len(dp)):
        if new <= dp[j]:
            dp[j] = new
            flag = 1
            break
    if flag == 0:
        dp.append(new)

print(len(dp))
