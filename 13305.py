import sys

n = int(sys.stdin.readline())
length = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))

res = 0
standard = 1000000001
for i in range(n-1):
    if price[i] < standard:
        standard = price[i]
    res += standard * length[i]

print(res)
