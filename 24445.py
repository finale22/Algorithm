import sys
from collections import deque


def bfs(graph, start, visited):
    res = []
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        res.append(v)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return res


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

res = bfs(graph, r, visited)
for i, e in enumerate(res):
    dict[e] = i + 1

for i in range(1, n+1):
    print(dict[i])
