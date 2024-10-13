import sys

k, n = map(int, input().split())
lan = []
for i in range(k):
    line = int(sys.stdin.readline())
    lan.append(line)

max_line = max(lan)
start, end = 0, max_line

while True:
    res = 0
    mid = (start + end) // 2
    if mid == 0:
        mid = 1
    for i in lan:
        tmp = i // mid
        res += tmp
    if res < n:
        end = mid - 1
    else:
        start = mid + 1
    if start > end:
        break

print(end)
