import sys
from collections import deque


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


sys.setrecursionlimit(100000)
n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    s, e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(1, n+1):
    graph[i] = sorted(graph[i])
    
visited = [False] * (n + 1)
dfs(graph, v, visited)
visited = [False] * (n + 1)
print('')
bfs(graph, v, visited)
