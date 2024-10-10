import sys

n = int(sys.stdin.readline())
f = [0] * (n + 1)

def fibonacci(n):
    f[1], f[2], count = 1, 1, 0
    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2]
        count += 1
    return f[n], count

a, c = fibonacci(n)
print(a, c)
