import sys


def merge(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = merge(array[:mid])
    right = merge(array[mid:])
    return merge_sort(left, right)


def merge_sort(left, right):
    lst = []
    left_id, right_id = 0, 0

    while len(left) > left_id and len(right) > right_id:
        if left[left_id] > right[right_id]:
            lst.append(right[right_id])
            right_id += 1
        else:
            lst.append(left[left_id])
            left_id += 1
    while len(left) > left_id and len(right) <= right_id:
        lst.append(left[left_id])
        left_id += 1
    while len(right) > right_id and len(left) <= left_id:
        lst.append(right[right_id])
        right_id += 1
    return lst


n = int(sys.stdin.readline())

meetings = []
for i in range(n):
    start, end = map(int, sys.stdin.readline().split())
    meetings.append((end, start))

meetings = merge(meetings)
end, start = meetings[0]
res = 1
if len(meetings) > 1:
    for i in range(1, n):
        end2, start2 = meetings[i]
        if start2 >= end:
            res += 1
            end, start = end2, start2

print(res)
