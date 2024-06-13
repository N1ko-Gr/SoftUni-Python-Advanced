from collections import deque

row, col = [int(x) for x in input().split()]
txt = deque(input())

matrix = []

for i in range(row):
    matrix.append([''] * col)
    for j in range(col):
        if i % 2 == 0:
            matrix[i][j] = txt[0]
        else:
            matrix[i][-1 - j] = txt[0]

        txt.rotate(-1)

[print(*row, sep='') for row in matrix]