import sys

n = int(sys.stdin.readline())

start, end = 0, n
while start <= end:
    mid = (start + end) // 2
    if mid**2 >= n:
        res = mid
        end = mid - 1
    else:
        start = mid + 1

print(res)
