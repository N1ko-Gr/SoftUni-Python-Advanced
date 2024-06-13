row, col = map(int, input().split())

matrix = []

start_index = ord('a')

for i in range(row):
    matrix.append([])
    for j in range(col):
        matrix[i].append(chr(start_index+i) + chr(i+start_index+j) + chr(start_index+i))

[print(' '.join(matrix[i])) for i in range(row)]