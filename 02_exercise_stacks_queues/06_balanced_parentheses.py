from collections import deque

line = deque(input())

open_parentheses = '({['
close_parentheses = ')}]'

couter = 0

while line and len(line) / 2 > couter:
    if line[0] in close_parentheses:
        break
    index = open_parentheses.index(line[0])
    if line[1] == close_parentheses[index]:
        line.popleft()
        line.popleft()
        line.rotate(couter)
        couter = 0
    else:
        line.rotate(-1)
        couter += 1

if line:
    print('NO')
else:
    print('YES')