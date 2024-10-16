import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
arr = []

start, end = 0, n * n
ans = 0
while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in range(1, n + 1):
        count += min(mid//i, n)
    if count >= k:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1

print(ans)
