import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))

dp = [arr[0]]
max_num = 0
for i in range(1, n):
    if i == 1:
        dp.append(arr[i - 1] + arr[i])
    elif i == 2:
        tmp = max(arr[i - 2] + arr[i], arr[i - 1] + arr[i])
        if tmp < max_num:
            tmp = max_num
        dp.append(tmp)
    else:
        tmp = max(dp[i - 2] + arr[i], dp[i - 3] + arr[i - 1] + arr[i])
        if tmp < max_num:
            tmp = max_num
        dp.append(tmp)
    max_num = dp[-1]

print(dp[-1])
