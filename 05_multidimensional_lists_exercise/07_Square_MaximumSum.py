row, col = [int(x) for x in input().split(', ')]

matrix = [[int(x) for x in input().split(', ')] for _ in range(row)]

max_sum = float('-inf')
max_row, max_col = 0, 0

for i in range(row - 1):
    for j in range(col - 1):
        current_sum = matrix[i][j] + matrix[i + 1][j] + matrix[i][j + 1] + matrix[i + 1][j + 1]

        if current_sum > max_sum:
            max_sum = current_sum
            max_row, max_col = i, j


print(f'{matrix[max_row][max_col]} {matrix[max_row][max_col + 1]}\n'
      f'{matrix[max_row + 1][max_col]} {matrix[max_row + 1][max_col + 1]}')
print(max_sum)


