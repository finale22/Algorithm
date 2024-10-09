import sys

n = int(sys.stdin.readline())
s = set()

for i in range(n):
    word = sys.stdin.readline().rstrip()
    s.add((len(word), word))

lst = list(s)
lst.sort()

for i in lst:
    length, word = i
    print(word)
