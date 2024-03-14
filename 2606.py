import sys
from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    res = -1
    while queue:
        v = queue.popleft()
        res += 1
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return res


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

print(bfs(graph, 1, visited))
