rows, cols = [int(n) for n in input().split(", ")]

matrix = []
sum_cols = 0

for i in range(rows):
    line = [int(n) for n in input().split()]
    matrix.append(line)

for column in range(cols):
    sum_cols =0
    for row in range(rows):
        sum_cols += matrix[row][column]

    print(sum_cols)




