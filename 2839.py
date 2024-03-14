import sys

n = int(sys.stdin.readline())

bag5 = n // 5
bag5_rest = n % 5
if (bag5_rest == 1 or bag5_rest == 2 or bag5_rest == 4) and bag5 > 1:
    bag5_rest = 0
    while n % 5 != 0:
        n -= 3
        bag5_rest += 3
    bag5 = n // 5
bag3 = bag5_rest // 3
bag3_rest = bag5_rest % 3
res = 0

if bag3_rest != 0:
    bag3_2 = n // 3
    bag3_2_rest = n % 3
    if bag3_2_rest == 0:
        res = bag3_2
    else:
        res = -1
else:
    res = bag5 + bag3

print(res)
