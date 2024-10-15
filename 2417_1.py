import sys, math
from decimal import Decimal, getcontext

getcontext().prec = 100
n = int(sys.stdin.readline())

print(math.ceil(Decimal(n)**Decimal(1/2)))
