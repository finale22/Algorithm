import sys

n, c = map(int, input().split())
arr =[]
for i in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort()

start, end = 0, arr[-1] - arr[0]
while start <= end:
    mid = (start + end) // 2
    count = 1
    pre_dist = arr[0]
    for i in range(1, len(arr)):
        if arr[i] - pre_dist >= mid:
            count += 1
            pre_dist = arr[i]
    if count < c:
        end = mid - 1
    else:
        res = mid
        start = mid + 1

print(res)
