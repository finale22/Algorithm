import sys

n = int(sys.stdin.readline())
prev1, prev2 = 1, 2
if n == 1:
    cur = prev1
elif n == 2:
    cur = prev2
else:
    for i in range(3, n+1):
        cur = (prev1 + prev2) % 15746
        prev1 = prev2
        prev2 = cur

print(cur)
