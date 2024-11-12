import sys

n = int(sys.stdin.readline())
arr = []
tree = []
for i in range(1, n+1):
    arr.append(list(map(int, input().split())))
    if i == 1:
        tree.append([0])
    elif i == 2:
        tree.append([0, 1])
    else:
        tmp = []
        for j in range(i):
            tmp.append(j)
            if 0 < j < i - 1:
                tmp.append(j)
        tree.append(tmp)

dp = [arr[0][0]]
for i in range(1, n):
    tree_lst = tree[i]
    arr_lst = arr[i]
    pre_idx = -1
    dp_idx = 0
    dp_idx_count = 0
    tmp = []
    for j in tree_lst:
        v = dp[dp_idx] + arr_lst[j]
        dp_idx_count += 1
        if dp_idx_count == 2:
            dp_idx += 1
            dp_idx_count = 0
        if pre_idx == j:
            max_v = max(v, tmp[-1])
            tmp[-1] = max_v
        else:
            tmp.append(v)
        pre_idx = j
    dp = tmp
print(max(dp))
