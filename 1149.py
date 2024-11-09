import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

dp = [[1001*1001, arr[0][0], arr[0][0]], [arr[0][1], 1001*1001, arr[0][1]], [arr[0][2], arr[0][2], 1001*1001]]
for i in arr[1:]:
    for j in range(3):
        for k in range(3):
            dp[j][k] += i[k]

    tmp = []
    for j in range(3):
        lst = [dp[0][j], dp[1][j], dp[2][j]]
        tmp.append(min(lst))

    for j in range(3):
        for k in range(3):
            if dp[j][k] <= 1000*1000:
                dp[j][k] = tmp[j]

print(min(tmp))
