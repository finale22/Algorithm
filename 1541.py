import sys

formula = sys.stdin.readline()

num = ''
minus_num, plus_num = 0, 0
symbol = '+'
for i in formula:
    if i != '+' and i != '-':
        num += i
    if i == '+' or i == '-':
        if symbol == '+':
            plus_num += int(num)
            num = ''
        else:
            minus_num += int(num)
            num = ''
        if i == '-':
            symbol = '-'
if symbol == '+':
    plus_num += int(num)
else:
    minus_num += int(num)

print(plus_num - minus_num)
