import sys

n = int(sys.stdin.readline())
dp = [0] * (n + 3)
dp[2], dp[3] = 1, 1
if n > 3:
    for i in range(4, n + 1):
        count = 0
        j = i
        while True:
            if dp[j] > 0:
                dp[i] = count + dp[j]
                break
            if j % 3 == 0 or j % 2 == 0:
                if j % 3 == 0 and j % 2 == 0:
                    if dp[j // 3] < dp[j // 2]:
                        tmp = j // 3
                    else:
                        tmp = j // 2
                elif j % 3 == 0 and j % 2 != 0:
                    tmp = j // 3
                else:
                    tmp = j // 2
                if dp[tmp] < dp[j - 1]:
                    j = tmp
                else:
                    j = j - 1
            else:
                j = j - 1
            count += 1

print(dp[n])
