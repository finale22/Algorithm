import sys


def dfs(graph, r, c, n, m):
    if c >= m or c <= -1 or r >= n or r <= -1:
        return False
    if graph[r][c] == 1:
        graph[r][c] = 0
        dfs(graph, r, c-1, n, m)
        dfs(graph, r-1, c, n, m)
        dfs(graph, r, c+1, n, m)
        dfs(graph, r+1, c, n, m)
        return True
    return False


sys.setrecursionlimit(10**6)
t = int(sys.stdin.readline())
res_lst = []
for i in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0] * m for _ in range(n)]
    loc = []
    for j in range(k):
        c, r = map(int, sys.stdin.readline().split())
        loc.append((r, c))
        graph[r][c] = 1
    loc = sorted(loc)
    res = 0
    for r, c in loc:
        if graph[r][c] == 0:
            continue
        dfs(graph, r, c, n, m)
        res += 1
    res_lst.append(res)

for i in res_lst:
    print(i)
