import sys

n = int(sys.stdin.readline())
n_lst = list(map(int, input().split()))
m = int(sys.stdin.readline())
m_lst = list(map(int, input().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n_lst.sort()

for i in m_lst:
    res = binary_search(n_lst, i, 0, len(n_lst)-1)
    if res != None:
        print(1)
    else:
        print(0)
