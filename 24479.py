import sys


def dfs(graph, v, visited, dfs_res):
    visited[v] = True
    dfs_res.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited, dfs_res)


sys.setrecursionlimit(10**6)
n, m, r = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]

visited = [False] * (n+1)
dfs_res = []
dict = {}

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(n):
    graph[i] = sorted(graph[i])

for i in range(n):
    dict[i+1] = 0

dfs(graph, r, visited, dfs_res)
for i, v in enumerate(dfs_res):
    dict[v] = i + 1

for i in range(1, len(dict)+1):
    print(dict[i])
