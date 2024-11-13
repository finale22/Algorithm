import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))

dp, step = [], 0
for i, e in enumerate(arr):
    if i == 0:
        dp.append(e)
    elif i == 1:
        dp.append(dp[i - 1] + e)
    elif i == 2:
        if arr[i - 2] > arr[i - 1]:
            dp.append(arr[i - 2] + e)
        else:
            dp.append(arr[i - 1] + e)
            step = 1
    else:
        if step == 1:
            if dp[i - 2] > arr[i - 1] + dp[i - 3]:
                dp.append(dp[i - 2] + e)
                step = 0
            else:
                dp.append(arr[i - 1] + dp[i - 3] + e)

        else:
            if dp[i - 2] > dp[i - 1]:
                dp.append(dp[i - 2] + e)
            else:
                dp.append(dp[i - 1] + e)
                step = 1

print(dp[-1])
