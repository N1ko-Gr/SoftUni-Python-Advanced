row, col = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for _ in range(row)]

max_sum = -float('inf')

start_row, start_col = 0, 0

for i in range(row - 2):
    for j in range(col - 2):

        current_sum = (matrix[i][j] + matrix[i + 1][j] + matrix[i][j + 1] + matrix[i + 1][j + 1] +
                       matrix[i + 2][j + 2] + matrix[i + 2][j] + matrix[i][j + 2] + matrix[i + 2][j + 1] +
                       matrix[i+1][j + 2])

        if current_sum > max_sum:
            max_sum = current_sum
            start_row, start_col = i, j


print(f'Sum = {max_sum}')
print(f'{matrix[start_row][start_col]} {matrix[start_row][start_col + 1]} {matrix[start_row][start_col + 2]}\n'
      f'{matrix[start_row + 1][start_col]} {matrix[start_row + 1][start_col + 1]} {matrix[start_row + 1][start_col + 2]}\n'
      f'{matrix[start_row+2][start_col]} {matrix[start_row+2][start_col + 1]} {matrix[start_row+2][start_col + 2]}')



