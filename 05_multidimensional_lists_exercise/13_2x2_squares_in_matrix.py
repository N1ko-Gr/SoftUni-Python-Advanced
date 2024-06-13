row, col = [int(x) for x in input().split()]

matrix = [[x for x in input().split()] for _ in range(row)]

acc = 0

for i in range(row-1):
    for j in range(col-1):
        if matrix[i][j] == matrix[i+1][j] and matrix[i][j] == matrix[i][j+1] and matrix[i][j] == matrix[i+1][j+1]:
            acc += 1


print(acc)