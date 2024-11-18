import sys
from bisect import bisect_left

def bitonic(num, array):
    seq = [array[0]]
    res = [len(seq)]
    for i in range(1, num):
        idx = bisect_left(seq, array[i])
        if idx >= len(seq):
            seq.append(array[i])
        else:
            seq[idx] = array[i]
        res.append(len(seq))
    return res

def result_dp(lis, lds):
    dp = []
    lds.reverse()
    for i in range(len(lis)):
        dp.append(lis[i] + lds[i] - 1)
    return max(dp)

n = int(sys.stdin.readline())
arr = list(map(int, input().split()))

dp_lis = bitonic(n, arr)
dp_lds = bitonic(n, arr[::-1])

print(result_dp(dp_lis, dp_lds))
