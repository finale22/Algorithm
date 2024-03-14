import sys


def dfs(graph, x, y, res_lst):
    if x >= n or x <= -1 or y >= n or y <= -1:
        return False
    if graph[y][x] == 1:
        graph[y][x] = 0
        dfs(graph, x - 1, y, res_lst)
        dfs(graph, x, y - 1, res_lst)
        dfs(graph, x + 1, y, res_lst)
        dfs(graph, x, y + 1, res_lst)
        res_lst.append([x, y])
        return True
    return False


n = int(sys.stdin.readline())
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))
res = 0
res_lst = []
count = []
for i in range(n):
    for j in range(n):
        if dfs(graph, j, i, res_lst):
            res += 1
            count.append(len(res_lst))
            res_lst = []

count = sorted(count)
print(res)
for i in count:
    print(i)
