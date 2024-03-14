import sys


def dfs(graph, v, visited, res):
    visited[v] = True
    res.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited, res)


sys.setrecursionlimit(10**6)
n, m, r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(n+1):
    graph[i] = sorted(graph[i], reverse=True)

dict = {}
for i in range(1, n+1):
    dict[i] = 0

res = []
dfs(graph, r, visited, res)

for i, e in enumerate(res):
    dict[e] = i + 1

for i in dict.keys():
    print(dict[i])
